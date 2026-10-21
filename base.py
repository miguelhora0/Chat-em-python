import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', 9999))

servidor.listen(1)
print("Server aguardando conexão da porta 9999. Aguarde... ")

conn, addr = servidor.accept()
print(f"Cliente Conectado: {addr[0]}:{addr[1]}")

while True:
    dados = conn.recv(1024)

    if not dados:
        print("Cliente desconectou.")
        break
    mensagem = dados.decode('utf-8')
    print(f"Cliente disse: {mensagem} ")
    
    resposta = input("Você: ")
    conn.send(resposta.encode('utf-8'))
    
conn.close()
servidor.close()

