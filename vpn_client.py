#author: Syd Tomas
#script for BlueCoat POC
import paramiko
import time
import sys
import re

print "*******************************************************************"
print "IP Address List:"
print "  India 5 - Initiator (certificate based auth)   - 172.26.47.4"
print "  Cape Verde - Initiator (PSK IP)                - 172.26.37.170"
print "  India6 - Initiator (PSK FQDN)                  - 172.26.47.5"
print "  India 7 - Initiator (Certificate based auth)   - 172.26.47.6"
print "  Echo7 - Initiator (PSK IP)                     - 172.26.47.134"
print "*******************************************************************"
print " "

vpnclient = raw_input("IP address of the router to access: ")
ip_address = vpnclient
username = "admin"
password = "cisco123"

if vpnclient == "172.26.47.4":
    interface = "Te0/1/0"
elif vpnclient == "172.26.37.170":
    interface = "Te0/0/0"
elif vpnclient == "172.26.47.5":
    interface = "Te0/1/0"
elif vpnclient == "172.26.47.6":
    interface = "Te0/1/0"
elif vpnclient == "172.26.47.134":
    interface = "Te0/1/0"
else:
    print "no interfaces match"


def inputletter():
    selection = raw_input("Please type 'shut' to shutdown interface, or 'noshut' to unshut interfaces: ")

    if selection == "shut":
        print "Shutting down sub interface for", vpnclient
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("enable\n")
        remote_connection.send("cisco123\n")
        remote_connection.send("terminal length 0\n")
        remote_connection.send("configure terminal\n")
        remote_connection.send("interface %s\n" % (interface))
        remote_connection.send("shut\n")
        time.sleep(1)
        #print "interface", interface
        remote_connection.send("exit\n")
        time.sleep(3)
        output = remote_connection.recv(65535)
        print output
        ssh_client.close
    elif selection == "noshut":
        print "Bringing up interface for", vpnclient
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("enable\n")
        remote_connection.send("cisco123\n")
        remote_connection.send("terminal length 0\n")
        remote_connection.send("configure terminal\n")
        remote_connection.send("interface %s\n" % (interface))
        remote_connection.send("no shut\n")
        time.sleep(1)
        remote_connection.send("exit\n")
        time.sleep(3)
        output = remote_connection.recv(65535)
        print output
    else:
        print "invalid selection"
inputletter()
