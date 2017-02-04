import socket
import time

g_is_debug = '1'
def dblog(*args, **kwargs):
	if g_is_debug == '1':
		print(*args, **kwargs)

ttl = 1
port = 33435 
max_ttl = 30
dest_addr = None
finish = 0
def main(dest_name):
	global ttl,port,max_ttl,dest_addr
	dest_addr = socket.gethostbyname(dest_name) 
	icmp_p = socket.getprotobyname("icmp")
	udp_p = socket.getprotobyname("udp")
	dblog("icmp_p = ", icmp_p, "udp_p =",  udp_p, "dest_addr=", dest_addr)


	dblog("come to while true")
	while True:
		#1.create socket with target of dest
		print("ttl :", ttl)
		send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 
		send_socket.bind(("", port)) #bind the special port
		#send_socket = socket.socket(socket.AF_INET, socket., udp_p) 
		#2.set TTL started with 1 ,then increment by each time
		send_socket.setsockopt(socket.SOL_IP,socket.IP_TTL, ttl)

		#3.send socket 

		data = bytes(("ttl" + str(ttl)), 'utf-8')
		send_socket.sendto(data,(dest_addr, port))
		
		time.sleep(1)
		send_socket.close()
		time.sleep(1)

		#5 until send successfully
		if finish ==1 or ttl >= max_ttl:
			break
		ttl += 1

	
	dblog("send finished with finish = ", finish , "ttl = ", ttl)


if __name__ == "__main__":
	print("trace routors")
	main("sina.com")
	print("end")