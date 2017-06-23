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

print "***********************************************"
print "Successful connection to ", ip_address
print "***********************************************"

remote_connection = ssh_client.invoke_shell()
remote_connection.send("terminal length 0\n")
remote_connection.send("configure terminal\n")

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
remote_connection.send("exit\n")

time.sleep(1)
output = remote_connection.recv(99999)
print output

ssh_client.close
