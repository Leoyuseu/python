import socket
import struct
from time import sleep,time,ctime

def main():
    MCAST_GRP = '224.1.1.1'
    MCAST_PORT = 5007
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    for i in range(200):
        sock.sendto(('Hello World!'*10).encode(), (MCAST_GRP, MCAST_PORT))
        sleep(1)

if __name__ == '__main__':
    main()
