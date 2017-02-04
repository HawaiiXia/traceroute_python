import socket
import traceroute
import os
g_is_debug = '1'
def dblog(*args, **kwargs):
	if g_is_debug == '1':
		print(*args, **kwargs)


def main():
	print("os name = ", os.name)
	if os.name =="nt":
		sock_protocl = socket.IPPROTO_IP
	else:
		sock_protocl = socket.IPPROTO_ICMP

	recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, sock_protocl)
	
	dblog("traceroute.port =", traceroute.port)
	
	
	recv_socket.bind(("", traceroute.port))
	recv_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	if os.name == "nt":
		#recv_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
		recv_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	while True:
			#3.2 recive icmp
		dblog("come to recvfrom")
		
		recv_data, cur_addr = recv_socket.recvfrom(1024)
		try:
			cur_name = socket.gethostbyaddr(cur_addr[0])
		except Exception as e:
			print(e)
			cur_name = '*'	
		dblog("recvfrom something : \n" , "recv_data: \n", recv_data, "cur_addr:\n", cur_addr)
		print(traceroute.ttl, "		", cur_name, cur_addr)
		dblog("traceroute.dest_addr:", traceroute.dest_addr)
		if traceroute.dest_addr == cur_addr[0] or traceroute.ttl >= traceroute.max_ttl:
			break

	traceroute.finish = 1
	dblog("rece finish with ttl = ", traceroute.ttl)
	if os.name == "nt":
		recv_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
	recv_socket.close()	

def test():
	print(traceroute.ttl)

if __name__ == "__main__":
	dblog("traceroute_recv start")
	#test()
	main()
