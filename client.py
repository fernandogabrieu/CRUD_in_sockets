import socket

socketDados = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = ('127.0.0.1',50001)
socketDados.connect(destino)

op = None

while op != '5':

    op = input('\nDigite:\n1 para Create\n2 para Read\n3 para Update\n4 para Delete\n5 para sair\nOpção: ')

    #Create
    if op == '1':
        print('\nCREATE')
        name        = input('Nome do país: ')
        capital     = input('Capital: ')
        continent   = input('Continente: ')
        language    = input('Idioma: ')
        population  = input('População: ')
        coin        = input('Moeda: ')
        
        message = "**".join([name, capital, continent, language, population, coin])
        socketDados.send(op.encode() + len(message.encode()).to_bytes(1,'big')  + message.encode())

        len_message = int.from_bytes(socketDados.recv(1),'big')
        message = socketDados.recv(len_message).decode()

        print(message)

    #Read
    elif op == '2':
        print('\nREAD')
        name = input('Nome do país: \n')

        message = "**".join([name])
        socketDados.send(op.encode() + len(message.encode()).to_bytes(1,'big')  + message.encode())

        len_message = int.from_bytes(socketDados.recv(1),'big')
        message = socketDados.recv(len_message).decode()
        print(message)

    #Update
    elif op == '3':
        print('\nUPDATE')
        
        name        = input('Nome do país a ser ATUALIZADO: ')
        capital     = input('Capital: ')
        continent   = input('Continente: ')
        language    = input('Idioma: ')
        population  = input('População: ')
        coin        = input('Moeda: ')
        
        message = "**".join([name, capital, continent, language, population, coin])
        socketDados.send(op.encode() + len(message.encode()).to_bytes(1,'big')  + message.encode())

        len_message = int.from_bytes(socketDados.recv(1),'big')
        message = socketDados.recv(len_message).decode()
        print(message)    

    elif op == '4':
        print('\nDELETE')
        
        name = input('Nome do país a ser DELETADO: ')

        message = "**".join([name])
        socketDados.send(op.encode() + len(message.encode()).to_bytes(1,'big')  + message.encode())

        len_message = int.from_bytes(socketDados.recv(1),'big')
        message = socketDados.recv(len_message).decode()
        print(message)    

    elif op == '5':
        socketDados.send(op.encode())

socketDados.close()
