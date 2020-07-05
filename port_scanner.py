import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print(
	'''
  _____   ____  _____ _______    _____  _____          _   _ _   _ ______ _____  
 |  __ \ / __ \|  __ |__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_|_| \_|_| \_|______|_|  \_\
 	'''
	)

host = input("Enter the IP you want to Scan> ")
port = int(input("Enter the Port you want to Scan> "))

def portScanner(port):
	if s.connect_ex((host, port)):
		print("The port is closed.")
	else:
		print("The port is open.")
portScanner(port)
