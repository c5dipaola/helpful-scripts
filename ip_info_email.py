#!/usr/local/bin/python

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
import requests
import json
import os

user = '<HOW EVER YOU DO USERNAMES>'
password = '<HOW EVER YOU DO PASSWORDS>'

ip_address = '<IP ADDRESS TO LOOKUP>'

api_url = requests.get('https://<YOUR IB SERVER>/wapi/v1.4.2/ipv4address?ip_address=' + ip_address, auth=(user,password), verify=False)
api_url_network = requests.get('https://<YOUR IB SERVER>/wapi/v1.4.2/network?contains_address=' + ip_address, auth=(user,password), verify=False)
data = json.loads(api_url.text)
data_network = json.loads(api_url_network.text)


def getNames(api_get_data):
    for string in api_get_data:
        return string['names']

def getNetwork(api_get_data):
    for network in api_get_data:
        return network.get('network')

def getNetInfo(api_dat_network):
    for net_info in api_dat_network:
        return net_info.get('comment')


print('Here is the info about the IP ' + ip_address + '.')
print('')
print('The IP ' + ip_address + ' is from the network ') + getNetwork(data) + (', "') + getNetInfo(data_network)  + ('"')
print('')
print('The DNS names associated with ' + ip_address + ' are:')
print '\n'.join(str(p) for p in getNames(data))
print('')

os_path = "/path/to/textfile"

with open(os.path.join(os_path, 'ip_info_%s.txt' % ip_address), 'w') as message:
    print >>message, ('')
    print >>message, ('Here is the info about the IP ' + ip_address + '.')
    print >>message, ('')
    print >>message, ('The IP ' + ip_address + ' is from the network ') + getNetwork(data) + (', "') + getNetInfo(data_network)  + ('"')
    print >>message, ('')
    print >>message, ('The DNS names associated with ' + ip_address + ' are:')
    print >>message, '\n'.join(str(p) for p in getNames(data))
    print >>message,('')

with open(os.path.join(os_path, 'ip_info_%s.txt' % ip_address), 'rb') as new_message:
    msg = MIMEText(new_message.read())
    msg['Subject'] = 'IP info for %s' % ip_address
    msg['From'] = 'IP Info Script'
    msg['To'] = 'Those who need to know'

server = smtplib.SMTP('<MY SERVER NAME OR IP>')
server.sendmail('', ['name@mycompany.com', 'anothername@company.com], msg.as_string())
server.quit()
