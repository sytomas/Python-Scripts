#author: Syd Tomas
#script for BlueCoat POC
#this script will change the state of the TE0/0/0 and subinterfaces to either an up or down state.
import paramiko
import time
import sys
import re


capeverde = "172.26.37.170"
capeverdeinterface = "Te0/0/0"
username = "admin"
password = "cisco123"

print "*******************************************************************"
print "Select Physical Interface: "
print "  TE0/0/0 = x"
print "  TE0/0/1 = y"
print "*******************************************************************"

whatint = raw_input(">: ")
if whatint == "x":
    h = "TE0/0/0"
elif whatint == "y":
    h = "TE0/0/1"
else:
    print "invalid selection"

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

tunrange = int(raw_input("input number of tunnels to %s: " % (g)))
tuncount = int(raw_input("input number of tunnels to %s @ a time: " % (g)))
sleeptime = int(raw_input("input time in seconds to sleep: "))
tcount = tuncount -1 
rtcount = tunrange + 1

print "%sting %d interfaces at a time and sleeping for %s seconds." % (g,tuncount,sleeptime)
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=capeverde,username=username,password=password)
remote_connection = ssh_client.invoke_shell()
remote_connection.send("enable\n")
remote_connection.send("cisco123\n")
remote_connection.send("terminal length 0\n")
remote_connection.send("configure terminal\n")
#print "*******************************************************************"
#print "Clearing Crypto Ike Sessions"
#print "*******************************************************************"
#print " "
#remote_connection.send("do clear cryp sess\n")
#time.sleep(2)
#print "*******************************************************************"
print "physical interface %s on cape verde will be %s" % (h,g)
print "*******************************************************************"
print " "
remote_connection.send("interface %s\n" % (h)) #Te0/0/0\n")
time.sleep(.75)
remote_connection.send(str(g) + "\n")
print "*******************************************************************"
print "%sting sub-interfaces, %d @ a time:" % (g,tuncount)
print "*******************************************************************"
print " "
for i in range(1,rtcount,tuncount):
    begnum = i
    subintnum = begnum + tcount
    #remote_connection.send("interface range Te0/0/0.%d - Te0/0/0.%s\n" % (i,subintnum))
    remote_connection.send("interface range %s.%d - %s.%s\n" % (h,i,h,subintnum))
    time.sleep(.75)
    remote_connection.send(str(g) + "\n")
    print "cape verde - interface TE0/0/0.%d to TE0/0/0.%d %s\n" % (begnum,subintnum,g)
#    print "cape verde - interface TE0/0/0.", begnum, " to TE0/0/0.", subintnum, " ", g + "\n"
    print "sleeping for %s seconds" % (sleeptime)
    time.sleep(sleeptime)
remote_connection.send("exit\n")
time.sleep(3)
output = remote_connection.recv(65535)
print output
ssh_client.close
 