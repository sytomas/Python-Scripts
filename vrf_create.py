#author: Syd Tomas
#script for BlueCoat POC
import paramiko
import time
import sys
import re

ip_address = "IP_ADDRESS" #<== Input ip address"
username = "LOGIN" #<== Change this value
password = "PWD" #<== Change this value

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("*"* 24)
print("Successful connection to "), ip_address
print("*"* 24)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("enable\n")
remote_connection.send("cisco123\n")
remote_connection.send("terminal length 0\n")
remote_connection.send("configure terminal\n")

#configure vrf
print "Creating VRF"
for i in range (1,100):
    print "Creating IVRF-%d" % (i)
    remote_connection.send("vrf definition IVRF-%d\n" % (i))
    remote_connection.send("address-family ipv4\n")
    remote_connection.send("exit-address-family\n")
    remote_connection.send("address-family ipv6\n")
    remote_connection.send("exit-address-family\n")
    remote_connection.send("exit\n")
    time.sleep(1)
remote_connection.send("exit\n")
print("*"* 24)
print("Creation of VRF successful")
print("*"* 24)


remote_connection.send("exit\n")
time.sleep(1)
output = remote_connection.recv(99999)
print(output)

ssh_client.close
