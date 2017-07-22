#author: Syd Tomas
#script for BlueCoat POC
import paramiko
import time
import sys
import re


capeverde = "172.26.37.170"
capeverdeinterface = "Te0/0/0"
username = "admin"
password = "cisco123"
addint = int(10)



print "*******************************************************************"
print "Select Action: "
print "  bring up interface = a"
print "  bring down interface = b"
print "*******************************************************************"
print " "
inputaction = raw_input(">: ")
if inputaction == "a":
    g = "no shut"
elif inputaction == "b":
    g = "shut"
else:
    print "invalid selection"

sleeptime = float(raw_input("input time in seconds to sleep: "))
print "bringing up 10 interfaces at a time and sleeping for ", sleeptime
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=capeverde,username=username,password=password)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("enable\n")
remote_connection.send("cisco123\n")
remote_connection.send("terminal length 0\n")
remote_connection.send("configure terminal\n")
print "physical interface Te0/0/0 on cape verde will be ", g
remote_connection.send("interface Te0/0/0\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print (g, "ing sub-interfaces - 10 @ a time:")
for i in range(1,91):
    intadd = ((%x + 10) % (i))
    remote_connection.send("interface range Te0/0/0.%d - Te0/0/0.", intadd "\n" % (i))
remote_connection.send("interface range Te0/0/0.1 - Te0/0/0.10\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.1 to TE0/0/0.10 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.11 - Te0/0/0.20\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
#remote_connection.send("no shut\n")
print "cape verde - interface TE0/0/0.11 to TE0/0/0.20 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.21 - Te0/0/0.30\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.21 to TE0/0/0.30 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.31 - Te0/0/0.40\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.31 to TE0/0/0.40 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.41 - Te0/0/0.50\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.41 to TE0/0/0.50 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.51 - Te0/0/0.60\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.51 to TE0/0/0.60 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.61 - Te0/0/0.70\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.61 to TE0/0/0.70 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.71 - Te0/0/0.80\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.71 to TE0/0/0.80 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.81 - Te0/0/0.90\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.81 to TE0/0/0.90 ", g
print "sleeping for ", sleeptime
time.sleep(sleeptime)
remote_connection.send("interface range Te0/0/0.91 - Te0/0/0.100\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "cape verde - interface TE0/0/0.91 to TE0/0/0.100 ", g
remote_connection.send("exit\n")
time.sleep(3)
output = remote_connection.recv(65535)
print output
ssh_client.close
 