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

print "*******************************************************************"
print "Select parameters to remove:"
print "  vrf"
print "  crypto"
print "  bdi"
print "  full"
print "*******************************************************************"
print " "

remote_connection = ssh_client.invoke_shell()
remote_connection.send("terminal length 0\n")
remote_connection.send("configure terminal\n")

def userselect():
    selection = raw_input("Select parameter: ")

    if selection == "vrf":
        print "Shutting down interface for", vpnclient
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        print "***********************************************"
        print "Successful connection to ", ip_address
        print "***********************************************"
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
    elif selection == "intstat":
        print "Interface Status for", vpnclient
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password)
        remote_connection = ssh_client.invoke_shell()
        remote_connection.send("enable\n")
        remote_connection.send("cisco123\n")
        remote_connection.send("terminal length 0\n")
        remote_connection.send("show ip int %s\n" % (interface))
        output = remote_connection.recv(65535)
        print output
    else:
        print "invalid selection"
userselect()





#remove Certificate Crypto Map profile
print "modifying Crypto Map Certificate Profile"
remote_connection.send("crypto ikev2 profile IKEv2_CERT\n")
for i in range (3,101):
    print "removing match remote statement for CMAP-Site" + str(i)
    remote_connection.send("no match certificate CMAP-Site%d\n" % (i))
    time.sleep(.5)
for i in range (3001,4001):
    print "removing match remote statement for CMAP-Site" + str(i)
    remote_connection.send("no match certificate CMAP-Site%d\n" % (i))
    time.sleep(.5)
print "*******************************************************************"
print "removal of crypto certificate profile match statement successful"
print "*******************************************************************"

#remove FQDN Crypto Map profile
print "modifying Crypto Map FQDN Profile"
remote_connection.send("crypto ikev2 profile IKEV2_FQDN\n")
for i in range (2003,2101):
    print "removing match remote statement for fqdn site%d.customer-1.org" % (i)
    remote_connection.send("no match identity remote fqdn site%d.customer-1.org\n" % (i))
    time.sleep(1)
print "********************************************************************"
print "removal of crypto fqdn profile match remote statement successful"
print "********************************************************************"

#remove certificate-based authentication
for i in range (3,101):
    print "removing certificate map CMAP-Site" + str(i)
    remote_connection.send("no crypto pki certificate map CMAP-Site%d\n" % (i))
    time.sleep(1)
for i in range (3001,4001):
    print "removing certificate map CMAP-Site" + str(i)
    remote_connection.send("no crypto pki certificate map CMAP-Site%d\n" % (i))
    time.sleep(1)
print "******************************************"
print "removal of certificate CMAP successful"
print "******************************************"


#removing VNI
print "Removing VNI's"
for i in range (100001,100101):
    remote_connection.send("no member vni %d\n" % (i))
    time.sleep(.5)
for i in range (101001,101101):
    remote_connection.send("no member vni %d\n" % (i))
    time.sleep(.5)
for i in range (102001,102101):
    remote_connection.send("no member vni %d\n" % (i))
    time.sleep(.5)
for i in range (103001,104001):
    remote_connection.send("no member vni %d\n" % (i))
    time.sleep(.5)
print "*******************************************************************"
print "removal of VNI successful"
print "*******************************************************************"

#removing Bridge Domain's
print "Removing Bridge Domains"
for i in range (1,101):
    print "removing bridge-domain" + str(i)
    remote_connection.send("no bridge-domain %d\n" % (i))
    time.sleep(.5)
for i in range (1001,1101):
    print "removing bridge-domain" + str(i)
    remote_connection.send("no bridge-domain %d\n" % (i))
    time.sleep(.5)
for i in range (2001,2101):
    print "removing bridge-domain" + str(i)
    remote_connection.send("no bridge-domain %d\n" % (i))
    time.sleep(.5)
for i in range (3001,4001):
    print "removing bridge-domain" + str(i)
    remote_connection.send("no bridge-domain %d\n" % (i))
    time.sleep(.5)
print "*******************************************************************"
print "removal of Bridge Domain successful"
print "*******************************************************************"

#removing VRF's
for i in range (1,101):
    remote_connection.send("no vrf definition IVRF-SITE%d\n" % (i))
    time.sleep(.5)
for i in range (1001,1101):
    remote_connection.send("no vrf definition vrf definition IVRF-SITE%d\n" % (i))
    time.sleep(.5)
for i in range (2001,2101):
    remote_connection.send("no vrf definition vrf definition IVRF-SITE%d\n" % (i))
    time.sleep(.5)
for i in range (3001,4001):
    remote_connection.send("no vrf definition vrf definition IVRF-SITE%d\n" % (i))
    time.sleep(.5)
print "*******************************************************************"
print "removal of VRF successful"
print "*******************************************************************"


remote_connection.send("exit\n")

time.sleep(1)
output = remote_connection.recv(99999)
print output

ssh_client.close
