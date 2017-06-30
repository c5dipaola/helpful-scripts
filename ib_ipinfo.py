#!/usr/local/bin/python
import requests
import json

#############################################
#  How to use this script:
#  You can gather the "user" as raw input or static variable
#  You can gather "password" using getpass or make it static (NOT recommended)
#  You can gather "ip_address" as raw input, static or add your own code to pull from other sources
#############################################

user = '<HOWEVER YOU DO THE USERNAME>'
password = '<HOWEVER YOU DO THE PASSWORD>'

ip_address = '<HOWEVER YOU GET THE IP ADDRESS>'

api_url = requests.get('https://<YOUR IB SERVER>/wapi/v1.4.2/ipv4address?ip_address=' + ip_address, auth=(user,password), verify=False)
data = json.loads(api_url.text)

for item in data:
    network = item.get('network')
    names = item.get('names')


def getNames(api_get_data):
    for string in api_get_data:
        for name in string.get('names'):
            print name

def getNetwork(api_get_data):
    for network in api_get_data:
        print network.get('network')

print('#######################################################')
print('')
print('Here is the info about the IP ' + ip_address + '.')
print('')
print('The network ' + ip_address + ' is part of is:')
getNetwork(data)
print('')
print('The DNS names associated with  ' + ip_address + ' are:')
getNames(data)
print('')
print('#######################################################')
