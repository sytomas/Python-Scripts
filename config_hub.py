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

#configure certificate-based authentication
for i in range (3,101):
    print "creating certificate map CMAP-Site" + str(i)
    remote_connection.send("crypto pki certificate map CMAP-Site%d 10\n" % (i))
    remote_connection.send("subject-name co cn = site%s.customer-1.org\n" % (i))
    time.sleep(1)
#for i in range (3001,4001):
#    print "creating certificate map CMAP-Site" + str(i)
#    remote_connection.send("crypto pki certificate map CMAP-Site%d 10\n" % (i))
#    remote_connection.send("subject-name co cn = site%s.customer-1.org\n" % (i))
#    time.sleep(1)
print "******************************************"
print "Creation of certificate CMAP successful"
print "******************************************"


#configure Certificate Crypto Map profile
remote_connection.send("crypto ikev2 profile IKEv2_CERT\n")
for i in range (3,101):
    print "creating match remote statement for CMAP-Site" + str(i)
    remote_connection.send("match certificate CMAP-Site%d\n" % (i))
    time.sleep(1)
#for i in range (3001,4001):
#    print "creating match remote statement for CMAP-Site" + str(i)
#    remote_connection.send("match certificate CMAP-Site%d\n" % (i))
#    time.sleep(1)
print "***************************************************************************"
print "Addition to crypto certificate profile match remote statement successful"
print "***************************************************************************"

#configure FQDN Crypto Map profile
print "Creating Crypto Map FQDN Profile"
#remote_connection.send("crypto ikev2 profile IKEV2_FQDN\n")
#for i in range (2003,2101):
#    print "creating match remote statement for fqdn site%d.customer-1.org" % (i)
#    remote_connection.send("match identity remote fqdn site%d.customer-1.org\n" % (i))
#    time.sleep(1)
#print "********************************************************************"
#print "Addition to crypto fqdn profile match remote statement successful"
#  print "********************************************************************"

remote_connection.send("exit\n")

time.sleep(1)
output = remote_connection.recv(99999)
print output

ssh_client.close
