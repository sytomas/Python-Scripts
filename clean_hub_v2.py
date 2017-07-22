#author: Syd Tomas
#script for BlueCoat POC
import paramiko
import time
import sys
import re

ip_address = "172.26.37.203"
username = "admin"
password = "cisco123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)
remote_connection = ssh_client.invoke_shell()

def userselect():
    startplace=int(raw_input("please input the number to start: "))
    stopplace=int(raw_input("Please input the number to stop: "))
    #remote_connection.send("enable\n")
    #remote_connection.send("cisco123\n")
    remote_connection.send("terminal length 0\n")
    remote_connection.send("configure terminal\n")
    for i in range (startplace,stopplace):
        print "removing configuration for Site" + str(i)
        remote_connection.send("interface nve1\n")
        time.sleep(1)
        remote_connection.send("no member vni 10%d\n" % (i))
        time.sleep(1)
        remote_connection.send("no bridge-domain %d\n" % (i))
        time.sleep(1)
        #remote_connection.send("interface BDI%d\n" % (i))
        #time.sleep(1)
        #remote_connection.send("no shut")
        #time.sleep(3)
        remote_connection.send("no interface BDI%d\n" % (i))
        time.sleep(1)
        remote_connection.send("no vrf definition IVRF-Site%d\n" % (i))
        time.sleep(1)
        print "******************************************"
        print "successfully removed Site" + str(i)
        print "******************************************"  
    remote_connection.send("exit\n")

time.sleep(1)
output = remote_connection.recv(99999)
print output

userselect()

ssh_client.close
