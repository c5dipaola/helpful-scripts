import re


def _unidiff_output(expected, actual):
    """
    Helper function. Returns a string containing the unified diff of two multiline strings.
    """

    import difflib
    expected=expected.splitlines(1)
    actual=actual.splitlines(1)

    diff=difflib.unified_diff(expected, actual)

    return ''.join(diff)

device_deviceipdotted = '10.1.1.1'

template = """set system syslog file changes apply-groups LOGGING-STANDARD
set system syslog file changes conflict-log any
set system syslog file changes change-log any
set system syslog file security apply-groups LOGGING-STANDARD
set system syslog file security security any
set system syslog file security firewall any
set system syslog file interactive apply-groups LOGGING-STANDARD
set system syslog file interactive authorization info
set system syslog file interactive user info
set system syslog file interactive interactive-commands any
set system syslog file interactive match "!(CHILD_|COMMIT_PROGRESS|EX-BCM PIC|BRCM_COS_HALP|pif_get_ifd)"
set system syslog file general apply-groups LOGGING-STANDARD
set system syslog file general daemon info
set system syslog file general ftp warning
set system syslog file general ntp warning
set system syslog file general kernel warning
set system syslog file general dfc warning
set system syslog file general pfe warning
set system syslog file general match "!(STP |<UpDown>|EX-BCM PIC|BRCM_COS_HALP|Bandwidth|krt_decode)"
set system syslog file logall any any
set system syslog file logall archive size 10m
set system syslog file logall archive files 10
set system syslog console any none"""

show_syslog = """set system syslog user * any emergency
set system syslog host 10.1.9.23 any any
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
set system syslog file FIREWALL_HITS firewall any
set system syslog file default-log-messages any info
set system syslog file default-log-messages match "(requested 'commit' operation)|(copying configuration to juniper.save)|(commit complete)|ifAdminStatus|(FRU power)|(FRU removal)|(FRU insertion)|(link UP)|transitioned|Transferred|transfer-file|(license add)|(license delete)|(package -X update)|(package -X delete)|(FRU Online)|(FRU Offline)|(plugged in)|(unplugged)|CFMD_CCM_DEFECT| LFMD_3AH | RPD_MPLS_PATH_BFD|(Master Unchanged, Members Changed)|(Master Changed, Members Changed)|(Master Detected, Members Changed)|(vc add)|(vc delete)|(Master detected)|(Master changed)|(Backup detected)|(Backup changed)|(interface vcp-)|(AIS_DATA_AVAILABLE)|BR_INFRA_DEVICE"
set system syslog file default-log-messages structured-data
set system syslog console any none""" + device_deviceipdotted


diff = _unidiff_output(template, show_syslog)
print("\n------  Here is the full 'DIFF' -------\n\n" + diff + "\n\n--------------------------------\n\n")
cmdlist = []
for line in diff.splitlines():
    # -- Look for lines starting with '+set' as those are the lines that are different from our template
    if "+set" in line:
        # -- Removes the '+' in front of the diffed line
        lineout = line.strip('+')
        # -- Doing this first or else you get the "NoneType" error in the re.search for lines without group 2 of the search
        if "syslog file" in lineout:
            logfile = re.search(r"(set )(system syslog file [\w+\d+\S+]+)(\s.*)", lineout).group(2)
            # -- To eliminate duplicate search results, we only add result of search to list if it's not already there.
            # -- Note that I started with a blank list like:  cmdlist = []
            if logfile not in cmdlist:
                # -- This adds the search results of "logfile" above to "cmdlist" if it does not already exist in the list
                cmdlist.append(logfile)
                # -- Here I just printed the list so you can see the values being added each time and only once
                print(cmdlist)

# -- Here we are pulling each value in that was appended to the list "cmdlist", adding "value" to the string and printing
print("\n\n")
for value in cmdlist: print("delete " + value)
