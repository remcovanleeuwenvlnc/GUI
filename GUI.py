#!/usr/bin/python3

import NETCONF
import PYEZ
from tkinter import *

root = Tk()
root.title("Check PPPoE status on SRX")
root.minsize(600,400)
root.configure(background="grey")

def retrieve_input():
    srx = textBox1.get("1.0","end-1c")
    usr = textBox2.get("1.0", "end-1c")
    pwd = textBox3.get("1.0", "end-1c")
    if (netconf.get() == 1):
        NETCONF.connect(srx, 830, usr, pwd)
        label4 = Label(root, text="WAN IP address is: " + NETCONF.interface_ip [0].text)
        label4.pack()
        label5 = Label(root, text="PPPoE session is: " + NETCONF.interface_status [0].text)
        label5.pack()
    elif (pyez.get() == 1):
        print("PYEZ")
        PYEZ.connect(srx, usr, pwd)
        label4 = Label(root, text="WAN IP address is: " + NETCONF.interface_ip [0].text)
        label4.pack()
        label5 = Label(root, text="PPPoE session is: " + NETCONF.interface_status [0].text)
        label5.pack()
    elif (netmiko.get() == 1):
        print("NETMIKO")
    else:
        print("Nothing selected")

label1 = Label(root, text="Enter IP address Juniper SRX:")
label1.pack()
textBox1 = Text(root, height=1, width=15)
textBox1.pack()

label2 = Label(root, text="Enter Username Juniper SRX:")
label2.pack()
textBox2 = Text(root, height=1, width=15)
textBox2.pack()

label3 = Label(root, text="Enter Password Juniper SRX:")
label3.pack()
textBox3 = Text(root, height=1, width=15)
textBox3.pack()

netconf = IntVar()
c1 = Checkbutton(root, text="NETCONF", variable=netconf)
c1.pack()
pyez = IntVar()
c2 = Checkbutton(root, text="PYEZ", variable=pyez)
c2.pack()
netmiko = IntVar()
c3 = Checkbutton(root, text="NETMIKO", variable=netmiko)
c3.pack()

buttonStatus = Button (root, height=1, width=10, text="Commit", command=lambda: retrieve_input())
buttonStatus.pack()

root.mainloop()