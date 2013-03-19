import socket
import math



HOST = '192.168.254.3'          # Endereco IP do Servidor
PORT = 5000            			# Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print 'Programa Somador de 0 ate N\n\n'

print 'Digite a quantidade de clientes que sao esperados:\n'
nClientes = raw_input();


listaPortasClientes = [];
i=0;

print 'Aguardando ',nClientes,' clientes';

while i < int(nClientes):
    msg, enderecoCliente = udp.recvfrom(1024)
    print msg,enderecoCliente,i;
    listaPortasClientes.append(enderecoCliente)
    i = i + 1

numeroN = 0;
while numeroN < int(nClientes):
	print 'Entre com o numero N desejado maior que o numero de clientes:\n'
	numeroN = raw_input();

parcela = int(math.ceil(float(numeroN)/float(nClientes)));

#enviar para todos
i = 0
numeroMinimo = 0
numeroMaximo = parcela;
while i < int(nClientes):
	udp.sendto (str(numeroMinimo), listaPortasClientes[i]) #minimo
	udp.sendto (str(numeroMaximo), listaPortasClientes[i]) #maximo
	print 'minimo enviado',numeroMinimo
	print 'maximo enviado',numeroMaximo
	numeroMinimo = numeroMaximo + 1;
	numeroMaximo = numeroMaximo + parcela;
	if numeroMaximo > int(numeroN):
		numeroMaximo = int(numeroN);
	i = i + 1;

somaFinal = 0;
i = 0
while i < int(nClientes):
    somaParcial, enderecoCliente = udp.recvfrom(1024)
    somaFinal = somaFinal + int(somaParcial)
    i = i + 1



print 'Resultado Final',somaFinal
print 'fim programa';
udp.close()