import socket
HOST = '192.168.254.3'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
udp.sendto ('Conectado com Sucesso', dest)

print ('Aguardando resposta do servidor')
numeroMinimo, enderecoServidor = udp.recvfrom(1024)
numeroMaximo, enderecoServidor = udp.recvfrom(1024)

print (f'Minimo: {numeroMinimo} Maximo:{numeroMaximo}')
numeroMinimo = int(numeroMinimo);
numeroMaximo = int(numeroMaximo);
somatorio = 0;
while numeroMinimo <= numeroMaximo:
	somatorio = somatorio + numeroMinimo;
	numeroMinimo = numeroMinimo + 1;

print(f'fim somatorio parcial:{somatorio}')
udp.sendto (str(somatorio), dest)
print ('fim programa')

udp.close()