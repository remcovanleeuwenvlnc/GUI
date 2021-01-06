#!/usr/bin/python3

# Python script to execute a RPC by PYEZ on SRX

import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

#hostname = input("Device hostname: ")
#junos_username = input("Junos OS username: ")
#junos_password = getpass("Junos OS or SSH key password: ")

def connect(srx, usr, pwd):
    dev = Device(host=hsrx, user=usr, passwd=pwd)
    try:
        dev.open()
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        sys.exit(1)
    except Exception as err:
        print (err)
        sys.exit(1)

    print (dev.facts)
    dev.close()

