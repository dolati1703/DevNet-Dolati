import telnetlib
import time
def read_terminal(telnet_connection):
	return telnet_connection.read_until(b'#').decode('utf-8')
def write_terminal(telnet_connection,string):
	tn.write(bytes(string, 'utf-8'))
def compare(f1,f2):
	c1=open(f1,"r")
	c2=open(f2,"r")
	for line1 in c1:
		for line2 in c2:
			if line1 == line2:
				print("SAME\n")
			else:
				print(line1 + line2)
			break
	c1.close()
	c2.close()

HOST = "localhost"
port=5000
file=open("routers")
for IP in file:
	IP = IP.strip()
	print("Geting running-config from Router " + (IP) +":"+ str(port))
	HOST = IP
	tn = telnetlib.Telnet(HOST,port)
	write_terminal(tn,"show run \r\n")
	output = read_terminal(tn)
	lines=output.splitlines()
	f=open("backup"+HOST+"-"+str(port),"w")
	f.write(output)
	port=port+1
	f.close()

compare("backup192.168.163.134-5000","backup192.168.163.134-5001")
