#!/usr/bin/env python
import ipcalc
import json
import requests
import re
import sys

######################################################################################
# This is a slight variation on the script that utilizes the ipcacl module to provide 
# the range of the network as well as gives a clear CIDR definition for he the network.
######################################################################################

# User Info
user = '<INFOBLOX USER ID>'
password = '<INFOBLOX PASSWORD>'

#ip_address = raw_input("What's the IP? (x.x.x.x): ")
ip_address = sys.argv[1]

api_url_ip = requests.get('https://<INFOBLOX IP>/wapi/v1.4.2/ipv4address?ip_address=' + ip_address, auth=(user,password), verify=False)
api_url_network = requests.get('https://<INFOBLOX IP>/wapi/v1.4.2/network?contains_address=' + ip_address, auth=(user,password), verify=False)
ip_data = json.loads(api_url_ip.text)
network_data = json.loads(api_url_network.text)

#Uncomment below if you want to see the output of what JSON is pulling.
#print (json.dumps(ip_data))
#print (json.dumps(network_data))

def getNames(api_get_data):
    for string in api_get_data:
        return string['names']

def getNetwork(api_get_data):
    for network in api_get_data:
        return network.get('network')

def getNetName(api_get_data):
    for net_name in (api_get_data):
        return net_name.get('comment')

network_address = getNetwork(ip_data)
#print ('The network address is: ' + network_address)

# Pull the CIDR notation for the netmask
net_cidr_pull = re.search(r'\/.*',getNetwork(ip_data))
if net_cidr_pull:
    net_cidr = net_cidr_pull.group(0)

# Below is the info that build the IP list from the above NetMRI gets.
subnet = ipcalc.Network(getNetwork(ip_data))
# Generate empty list
AddrList = []
# Use the calculator to build a list of all the IP addresses
for x in ipcalc.Network(getNetwork(ip_data)):
    AddrList.append(str(x))

print('######################################################')
print('')
print('IP '+ ip_address + ' Is part of ' + getNetwork(ip_data) + " - " + '"{}"'.format(getNetName(network_data)))
print('Mask: ' + str(subnet.netmask()) + ' which is a ' + net_cidr)
print('Address Range: '+ AddrList[0] + " - " + AddrList[-1])
print('')
print('The DNS names associated with  ' + ip_address + ' are:')
print('\n'.join(str(p) for p in getNames(ip_data)))
print('######################################################')
