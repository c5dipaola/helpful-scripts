import re

# The 2 "cli_output" variables below represent the out of the CLI command "show high-availability state".
#
# "cli_output_1" is the output from a PA device that is not part of an HA pair.  In this case, it's considered
# a stand-alone device, so we would run all of our commands against it.
#
# "cli_output_2" is the output from the PASSIVE unit of an HA pair.  You can tell by looking at the 6th line down or so
# where it says "State: passive (last XX days)".  Then if you go down further, you will see under the
# "Peer Information:" where it says "State: active (last XX days)", meaning that this units neighbor is the active
# unit in the pair.
#
# It's important to note that these variables really would be just one variable in real code.  You should create a
# variable that runs the command (using "netmri_easy" or Netmiko) "show high-availability state" against the PAs.
# An example would be "show_state = easy.send_command('show high-availability state')".  Then you would use
# the variable "show_state" as the input argument for the function below called "pa_ha_state()".


cli_output_1 = '''

HA not enabled
'''

cli_output_2 = '''
Group 2:
  Mode: Active-Passive
  Local Information:
    Version: 1
    Mode: Active-Passive
    State: passive (last 19 days)
    Device Information:
      Management IPv4 Address: 1.2.3.2/24
      Management IPv6 Address:
      Jumbo-Frames enabled; MTU 1500
    HA1 Control Links Joint Configuration:
      Encryption Enabled: no
    Election Option Information:
      Priority: 1
      Preemptive: no
    Version Compatibility:
      Software Version: Match
      Application Content Compatibility: Match
      Anti-Virus Compatibility: Match
      Threat Content Compatibility: Match
      VPN Client Software Compatibility: Match
      Global Protect Client Software Compatibility: Match
    State Synchronization: Complete; type: ethernet
  Peer Information:
    Connection status: up
    Version: 1
    Mode: Active-Passive
    State: active (last 19 days)
    Device Information:
      Management IPv4 Address: 1.2.3.1/24
      Management IPv6 Address:
      Jumbo-Frames enabled; MTU 1500
      Connection up; Primary HA1 link
      Keep-alive config off; status up; Primary HA2 Link
        Monitor Hold inactive; Allow settling after failure
    Election Option Information:
      Priority: 100
      Preemptive: no
  Configuration Synchronization:
    Enabled: yes
    Running Configuration: synchronized
'''

# Here we created a definition (a.k.a. function) that can be reused that does the actual "screen scraping" to
# determine if the unit is active or passive.  This function would be called later PRIOR to running any commands
# against a PA device to check if it's the active or stand-alone unit or not.  The result of this definition is
# either "True" or "False" and is meant to be used in an "IF" or "WHILE" statement.
#
# You'll see a note in the line "cli_iter" that says to only iterate through the first 10 lines.  This is needed
# for the CLI output of PA devices in an HA pair because the search string is looking for the string "active".  The
# CLI output from an HA pair shows both the local and peer HA state, so if both units are up and functional, then
# there would always be an "active" unit in the pair.  So, since we only want to know the local unit's HA state, and
# the local unit state info is in the first 10 lines of the output, we don't want to check any more of the output or
# else we would always get the result that an active unit is present.

def pa_ha_state(clioutput):
    cli_comp_active = re.compile('(.*)(State:\s+active)(.*)')
    cli_comp_notenabled = re.compile('HA not enabled')
    cli_iter = iter(clioutput.splitlines()[:10]) # Only iterate through first 10 lines of CLI output
    for line in cli_iter:
        haenabled = cli_comp_active.search(line)
        hanotenabled = cli_comp_notenabled.search(line)
        if haenabled:
            active = haenabled.group(2)
            if active:
                return True
            else:
                return False
        elif hanotenabled:
            not_enabled = hanotenabled.group(0)
            if not_enabled:
                return True
            else:
                return False


# Below shows a simple test using the function "pa_ha_state()" in an "IF" statement to determine the HA state
# of a PA device.  This example below just uses the multi-line strings as variables at the top of the script
# and then just prints out the results of the definition.  In production, you would do something more along the lines
# of of an "IF" or "WHILE" statement saying if the result of the "pa_ha_state()" function is True, then run your code
# and if not ("else or elif") then don't run your code.

print("\n" * 3)
if pa_ha_state(cli_output_1):
    print("ACTIVE UNIT or SAUK PAN")
else:
    print("PASSIVE or NON-HA UNIT")

print("\n" * 3)
if pa_ha_state(cli_output_2):
    print("ACTIVE UNIT or SAUK PAN")
else:
    print("PASSIVE or NON-HA UNIT")

# One final note.  We use this by adding it to our own "NetDefs" python library that can be called by any other scripts
# you create.

