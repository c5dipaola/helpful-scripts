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

ip_address = raw_input('Enter the IP Address to look up: ')

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

###########################################################################################################################
# The below print statements print out the info about the IP address to your console screen
#   NOTE: This information will also be put in a .txt file on your local machine and then e-mailed out.
###########################################################################################################################

print('Here is the info about the IP ' + ip_address + '.')
print('')
print('The IP ' + ip_address + ' is from the network ') + getNetwork(data) + (', "') + getNetInfo(data_network)  + ('"')
print('')
print('The DNS names associated with ' + ip_address + ' are:')
print '\n'.join(str(p) for p in getNames(data))
print('')

###########################################################################################################################
# The below statements do the following:
#  First, the "os_path" defines the path to the local directory that a small text file will be created and stored.  This
#    text file will then be opened and read into the body of the e-mails message.
#  The first "with open..." stanza is the new file being opened up.  The "print" statements are actually printing those lines
#    into the new text file.  The text file will be named "ip_info_<ip_address>.txt", where <ip_address>
#    is the IP that was input into the "ip_address" input above.
#  Next, the second "with open..." statement reads the information from the file created in the first "with open.." statement
#    and uses it for the body of the message.  The parameters are then set for the actual e-mail message.
#      NOTE:  You can checn the Subject, From, and To to what you like.  Note that the From and To lines just show a string
#             in the e-mail's From and To lines.  You define the actual addressees further down.
###########################################################################################################################

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

###########################################################################################################################
# The below statements do the following:
#  First, set your SMTP mail relay server in the server = smtplib.SMTP('<MY SERVER NAME OR IP>'), replacing
#    <MY SERVER NAME OR IP> with your actual server name/IP.
#  Next, in the server.sendmail(...) section, do the following:
#     - First part, '<SENDER ADDRESS>' = You only need this if your server requires it.  Or else just put empty quotations ""
#     - Next is the Recipients.  Add as many reciepients as you want sepereted by comma (like 'me@company.com', 'you@company.com')
#     - Finally, msg.as_string() = If you changed the name of the variable "msg" above, then just use that and include the
#                                   .as_string() extenstion.  Otherwise, just leave it.
#  Last, you issue server.quit() to close out the server call.
###########################################################################################################################

server = smtplib.SMTP('<MY SERVER NAME OR IP>')
server.sendmail('<SENDER ADDRESS>', ['<RECIPIENT@ADDRESS>', '<ANOTHER@ADDRESS>'], msg.as_string())
server.quit()
