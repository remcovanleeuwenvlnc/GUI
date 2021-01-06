#!/usr/bin/python3

# Python script to fetch interface IP address and operation status through NCCLIENT (netconf)
import sys

import logging

from ncclient import manager


def connect(host, port, user, password):
    conn = manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           timeout=60,
                           device_params={'name': 'junos'},
                           hostkey_verify=False)

    rpc = "<get-interface-information><interface-name>pp0.0</interface-name></get-interface-information>"
    response = conn.rpc(rpc)

    global interface_status
    global interface_ip
    interface_status = response.xpath('//logical-interface/pppoe-information/pppoe-interface/state')
    interface_ip = response.xpath('//logical-interface/address-family/interface-address/ifa-local')

#if __name__ == '__main__':
#    LOG_FORMAT = '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s'
#    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=LOG_FORMAT)

#    connect('192.168.1.254', 830, 'admin', 'Astra14')