import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_servidor = input("IP do servidor: ")

cliente.connect((f"{ip_servidor}", 9999))
print("Conectado ao servidor!")

while True:
    mensagem = input(f"Você: ") 
    cliente.send(mensagem.encode('utf-8'))
    
    resposta = cliente.recv(1024).decode('utf-8')
    print(f"Servidor disse: {resposta}")

cliente.close()