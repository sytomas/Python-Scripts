#!/usr/bin/python2.7
import telnetlib
import time
#Start the timer
#Host to connect to
#HOST = "172.26.37.203"
HOST = raw_input(" Please enter IP address: ")
tn = telnetlib.Telnet(HOST)
a=tn.read_until("#")
print "time,ikev2_SA,ipsec_SA,cpu,CACincomingSA"
watch1=time.time()
for i in range (1,2000):
    watch=time.time()
    #Get the show crypto eli#
    tn.write(b"show crypto eli\n")
    b= tn.read_until("moth#")
    #Split crypto eli
    c=b.split()
    #Extract amount of phase II
    ipsec=c[33]
    #Extract amount of Phase I
    tn.write("show crypto ikev2 stats | i active\n")
    b= tn.read_until("moth#")
    d=b.split()
    ikev2=d[14]
    mytimer=watch-watch1
    #get the cpu
    tn.write(b"sh proc cpu | i util\n")
    b=tn.read_until("moth#")
    d=b.split()
    cpu=d[11]
    realcpu=cpu.split('%')
    cpu=realcpu[0]
    tn.write(b"show crypto ikev2 stats | i Total incoming IKEv2 SA Count\n")
    b=tn.read_until("moth#")
    e=b.split()
    incomingike=e[-2]
    #tn.write(b"show crypto ikev2 stats priority\n")
    #b=tn.read_until("moth#")
    #f=b.split()
    #LOWEST=f[-3]
    #LOW=f[-9]
    #HIGH=f[-15]
    #HIGHEST=f[-21]
    #print "%d,%s,%s,%s,%s,%s,%s,%s,%s" % (mytimer,ikev2,ipsec,cpu,incomingike,LOWEST,LOW,HIGH,HIGHEST)
    print "%d,%s,%s,%s,%s" % (mytimer,ikev2,ipsec,cpu,incomingike)
    time.sleep(1)
