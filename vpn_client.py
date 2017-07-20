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
    vpnhostname = "india5"
    begrangeselect = "1"
    endrangeselect = "101"
elif vpnclient == "172.26.37.170":
    interface = "Te0/0/0"
    vpnhostname = "cape verde"
    begrangeselect = "1001"
    endrangeselect = "1101"
elif vpnclient == "172.26.47.5":
    interface = "Te0/1/0"
    vpnhostname = "india6"
    begrangeselect = "2001"
    endrangeselect = "2101"
elif vpnclient == "172.26.47.6":
    vpnhostname = "india7"
elif vpnclient == "172.26.47.134":
    interface = "Te0/1/0"
    vpnhostname = "echo7"
    begrangeselect = "3001"
    endrangeselect = "4001"
else:
    print "no interfaces match"

print "*******************************************************************"
print "Select Action: "
print "  Interface Config = a"
print "  Configure VPN Client Router = b"
print "*******************************************************************"
print " "
inputaction = raw_input(">: ")

def intletter():
    selection = raw_input("Please type 'shut' to shutdown interface, 'noshut' to unshut interfaces: ")

    if selection == "shut":
        print "Shutting down interface for", vpnclient
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
        remote_connection.send("do clear cryp sess\n")
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
        #remote_connection.send("do clear cryp sess\n")
        time.sleep(1)
        remote_connection.send("exit\n")
        time.sleep(3)
        output = remote_connection.recv(65535)
        print output
    else:
        print "invalid selection"

def custconfig()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("enable\n")
    remote_connection.send("cisco123\n")
    remote_connection.send("terminal length 0\n")
    remote_connection.send("configure terminal\n")
    for a in range(begrangeselect,endrangeselect):
        print "creating PKI Trustpoint for Site" + str(a)
        remote_connection.send("crypto pki trustpoint tp-site%d 10\n" % (a))
        time.sleep(1)
        remote_connection.send("enrollment url http://172.26.39.124:80")
        time.sleep(1)
        remote_connection.send("subject-name CN=site%d.customer-1.org " % (a))
        time.sleep(1)
        remote_connection.send("vrf Mgmt-intf")
        time.sleep(1)
        remote_connection.send("revocation-check none")
        time.sleep(1)
        remote_connection.send("rsakeypair ciscopocsa-server")
        time.sleep(1)
        print "********************************************************************"
        print "Certificate Trustpoint Successful"
        print "********************************************************************"
        print "..\n"
        print "..\n"
        print "********************************************************************"
        print "creating VRF  for Site" + str(a)
        print "********************************************************************"
        #configure vrf
        print "Creating IVRF-Site%d" % (i)
        remote_connection.send("vrf definition IVRF-Site%d\n" % (i))
        time.sleep(1)
        remote_connection.send("address-family ipv4\n")
        time.sleep(1)
        remote_connection.send("exit-address-family\n")
        time.sleep(1)
        remote_connection.send("address-family ipv6\n")
        time.sleep(1)
        remote_connection.send("exit-address-family\n")
        time.sleep(1)
        remote_connection.send("exit\n")
        time.sleep(1)
        print "********************************************************************"
        print "Creation of VRF successful"
        print "********************************************************************"
        print "..\n"
        print "..\n"
        print "********************************************************************"
        print "creating crypto map for Site" + str(a)
        print "********************************************************************"
        if vpnhostname =="india5"
            for a in range(begrangeselect,endrangeselect):
            remote_connection.send("crypto ikev2 profile IKEv2_CERT-site%d" % (a))
            time.sleep(1)
            remote_connection.send("match fvrf IVRF-SITE%d" % (a))
            time.sleep(1)
            remote_connection.send("identity local fqdn site%d.customer-1.org", % (a))
            time.sleep(1)
            remote_connection.send("authentication local rsa-sig")
            time.sleep(1)
            remote_connection.send("authentication remote rsa-sig")
            time.sleep(1)
            remote_connection.send("pki trustpoint tp-site%d", % (a))
            time.sleep(1)
            remote_connection.send("crypto ipsec profile IPSEC_CERT-site%d", % (a))
            time.sleep(1)
            remote_connection.send("set transform-set TS")
            time.sleep(1)
            remote_connection.send("set ikev2-profile IKEv2_CERT-site%d", % (a))
            time.sleep(1)
        elif vpnhostname == "india6":
            for a in range(begrangeselect,endrangeselect):
                print "creating fqdn for FQDN site" + str(a)
                remote_connection.send("crypto ikev2 profile IKEV2_FQDN-site%d\n" % (a))
                remote_connection.send("")
        #creat subinterface
        print "creating sub-interface" + str(a)
        for i in (begrangeselect,endrangeselect,4)
            remote_connection.send("")
        interface TenGigabitEthernet0/1/0.3
 encapsulation dot1Q 3
 vrf forwarding IVRF-SITE3
 ip address 191.1.1.10 255.255.255.252
 shutdown
        #configure BDI
        print "Creating BDI Interface%d" % (i)
        remote_connection.send("Interface BDI%d\n" % (i))
        remote_connection.send("bandwidth 10000\n")
        remote_connection.send("vrf forwarding IVRF-Site%d\n" % (i))
        time.sleep(1)
        print "********************************************************************"
        print "Creation of BDI successful"
        print "********************************************************************"

        #configure NVE
        print "Creating NVE Interfaces"
        remote_connection.send("Interface nve1\n")
        print "Creating NVE Interface%d" % (i)
        remote_connection.send("member vni %d\n" % (i))
        remote_connection.send("bandwidth 10000\n")
        remote_connection.send("ingress-replicastion 172.16.0.2\n")
        time.sleep(1)
        print "********************************************************************"
        print "Creation of NVE successful"
        print "********************************************************************"

        #configure certificate-based authentication
       
            



#configure Certificate Crypto Map profile
#remote_connection.send("crypto ikev2 profile IKEv2_CERT\n")
#for i in range (1,8001):
#    print "creating match remote statement for CMAP-Site" + str(i)
#    remote_connection.send("match certificate CMAP-Site%d\n" % (i))
#    time.sleep(1)
#print "***************************************************************************"
#print "Addition to crypto certificate profile match remote statement successful"
#print "***************************************************************************"

#configure FQDN Crypto Map profile
print "Creating Crypto Map FQDN Profile"
remote_connection.send("crypto ikev2 profile IKEV2_FQDN\n")
#for i in range (4001,8001):
for i in range (5501,8001):
    print "creating match remote statement for fqdn site%d.customer-1.org" % (i)
    remote_connection.send("match identity remote fqdn site%d.customer-1.org\n" % (i))
    time.sleep(1)
remote_connection.send("exit\n")
print "********************************************************************"
print "Addition to crypto fqdn profile match remote statement successful"
print "********************************************************************"

#configure subinterface
        print "configuring subinterface for", vpnclient
        remote_connection.send("interface %s.%d" % (interface) % (begrangeselect))
        remote_connection.send("shut\n")
        time.sleep(1)

        #print "interface", interface
        remote_connection.send("exit\n")
        time.sleep(3)
        output = remote_connection.recv(65535)
        print output
        ssh_client.close


if inputaction == a:
    intletter()
else:
    custconfig()
