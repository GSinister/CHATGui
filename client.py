import socket 

print('''


    ____       __     _ _____          
   / __ )___  / /___ ( ) ___/___  _____
  / __  / _ \/ /_  / |/\__ \/ _ \/ ___/
 / /_/ /  __/ / / /_  ___/ /  __/ /__  
/_____/\___/_/ /___/ /____/\___/\___/  
                                       
				Code By GSinister
			https://github.com/GSinister


	''')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 9001
client_socket.connect((host, port))
nom = input("Quelle est votre nom ? ")

while True:

	message = input(f"{nom} > ")
	client_socket.send(f"{nom} > {message}".encode("utf-8"))