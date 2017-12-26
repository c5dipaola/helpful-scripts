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
CIDR_IP_Breakdown = collections.namedtuple('CIDR_IP_Breakdown', ['vip', 'dc1_dev1', 'dc1_dev2', 'dc2_dev1', 'dc2_dev2', 'mask', 'cidr'])

# Below are the CIDR breakdown using the named tuple above.  In this example, we are doing the math to get the VIP
# address (could be VRRP, HSRP or whatever) shared among 4 devices.  "dc1_dev1" would be Device 1 in Datacenter 1,
# "dc1_dev2" would be Device 2 in Datacenter 1, and so on.
cidr23 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 510), dc1_dev1=NumToIP(IPToNum(ip_in) + 509), dc1_dev2=NumToIP(IPToNum(ip_in) + 508),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 507), dc2_dev2=NumToIP(IPToNum(ip_in) + 506), mask='255.255.254.0', cidr='/23')
cidr24 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 254), dc1_dev1=NumToIP(IPToNum(ip_in) + 253), dc1_dev2=NumToIP(IPToNum(ip_in) + 252),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 251), dc2_dev2=NumToIP(IPToNum(ip_in) + 250), mask='255.255.255.0', cidr='/24' )
cidr25 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 126), dc1_dev1=NumToIP(IPToNum(ip_in) + 125), dc1_dev2=NumToIP(IPToNum(ip_in) + 124),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 123), dc2_dev2=NumToIP(IPToNum(ip_in) + 121), mask='255.255.255.128', cidr='/25')
cidr26 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 62), dc1_dev1=NumToIP(IPToNum(ip_in) + 61), dc1_dev2=NumToIP(IPToNum(ip_in) + 60),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 59), dc2_dev2=NumToIP(IPToNum(ip_in) + 58), mask='255.255.255.192', cidr='/26')
cidr27 = CIDR_IP_Breakdown(vip=NumToIP(IPToNum(ip_in) + 30), dc1_dev1=NumToIP(IPToNum(ip_in) + 29), dc1_dev2=NumToIP(IPToNum(ip_in) + 28),
                           dc2_dev1=NumToIP(IPToNum(ip_in) + 27), dc2_dev2=NumToIP(IPToNum(ip_in) + 26), mask='255.255.255.224', cidr='/27')

# Below is an example of a simple usage of the above named tuple application.
print(cidr24.dc1_dev1 + cidr24.cidr + " with a subnet mask of " + cidr24.mask + "and the gateway of " + cidr24.vip)
