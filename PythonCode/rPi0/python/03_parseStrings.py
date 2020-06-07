# Parse string data 

# Example string
message="""lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1034  bytes 78589 (76.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1034  bytes 78589 (76.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 130.64.95.120  netmask 255.255.255.0  broadcast 130.64.95.255
        inet6 fe80::299c:f74f:9940:70c1  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:68:fd:a1  txqueuelen 1000  (Ethernet)
        RX packets 2345  bytes 176460 (172.3 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6828  bytes 8258749 (7.8 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0"""

print(message)

# Split the string into two parts right at 'wlan0'
ip = message.split('wlan0')

# We need the 2nd part of the list, so we are using [1]
print(ip[1])
# Split the string into two parts right at 'inet'
ip = ip[1].split('inet')

# We need the 2nd part of the list, so we are using [1]
print(ip[1])

# Split the string into two parts right at ' '
ip = ip[1].split(' ')
# We need the 2nd part of the list, so we are using [1]
ip=ip[1]
print(ip)
