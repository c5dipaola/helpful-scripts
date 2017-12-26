import collections
import socket
import struct

def IPToNum(ip):
    """convert decimal dotted quad string to long integer"""
    return struct.unpack('>L', socket.inet_aton(ip))[0]


def NumToIP(n):
    "convert long int to dotted quad string"
    return socket.inet_ntoa(struct.pack('>L', n))


# This is the input IP address.  This could be any type of input, like "raw_input", API calls, etc...  The variable
# "ip_in" should stay the same unless you are modifying it throughout all the named tuple lines.
ip_in = '10.1.0.0'

# This is the named tuple that will be called and set up as the CIDR breakdowns in the next stanza
CIDR_IP_Breakdown = collections.namedtuple('Cidr_IP_Brkdwn', ['vip', 'dc1_dev1', 'dc1_dev2', 'dc2_dev1', 'dc2_dev2'])

# Below are the CIDR breakdown using the named tuple above.  In this example, we are doing the math to get the VIP
# address (could be VRRP, HSRP or whatever) shared among 4 devices.  "dc1_dev1" would be Device 1 in Datacenter 1,
# "dc1_dev2" would be Device 2 in Datacenter 1, and so on.
cidr23 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 510), dc1_dev1=NumToIP(IPToNum(ip_in) + 509), dc1_dev2=NumToIP(IPToNum(ip_in) + 508),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 507), dc2_dev2=NumToIP(IPToNum(ip_in) + 506))
cidr24 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 254), dc1_dev1=NumToIP(IPToNum(ip_in) + 253), dc1_dev2=NumToIP(IPToNum(ip_in) + 252),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 251), dc2_dev2=NumToIP(IPToNum(ip_in) + 250))
cidr25 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 126), dc1_dev1=NumToIP(IPToNum(ip_in) + 125), dc1_dev2=NumToIP(IPToNum(ip_in) + 124),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 123), dc2_dev2=NumToIP(IPToNum(ip_in) + 121))
cidr26 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 62), dc1_dev1=NumToIP(IPToNum(ip_in) + 61), dc1_dev2=NumToIP(IPToNum(ip_in) + 60),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 59), dc2_dev2=NumToIP(IPToNum(ip_in) + 58))
cidr27 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 30), dc1_dev1=NumToIP(IPToNum(ip_in) + 29), dc1_dev2=NumToIP(IPToNum(ip_in) + 28),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 27), dc2_dev2=NumToIP(IPToNum(ip_in) + 26))

# Below is an example of a simple usage of the above named tuple application.
print(cidr24.dc1_dev1)
print(cidr23.dc1_dev1)
