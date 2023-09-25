import socket

servidorConexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
porta = 50001
endereco = (ip, porta)
servidorConexao.bind(endereco)

servidorConexao.listen(1)
[socketDados, dadosCliente] = servidorConexao.accept()

op = None
countries = []

#################################################################################
#################################################################################
def create(message_received, list_of_countries):
    name = message_received[0]

    for country in list_of_countries:
        if name.lower() == country[0].lower():
            resposta = ('Já esta cadastrado.')
            return resposta

    capital    = message_received[1]
    continent  = message_received[2]
    language   = message_received[3]
    population = message_received[4]
    coin       = message_received[5]

    country = [name, capital, continent, language, population, coin]
    list_of_countries.append(country)

    resposta = ('Cadastrado com Suscesso.')
    return resposta
#################################################################################
#################################################################################
def read(message_received, list_of_countries):
    
    name = message_received[0]

    for country in list_of_countries:
        if name.lower() == country[0].lower():
            resposta = ('Registro encontrado: ' + str(country))
            return resposta
        
    resposta = 'Registro não encontrado.'
    return resposta
#################################################################################
#################################################################################
def update(message_received, list_of_countries):
    
    name = message_received[0]

    for country in list_of_countries:
        if name.lower() == country[0].lower():
            country[0]    = message_received[0]
            country[1]    = message_received[1]
            country[2]    = message_received[2]
            country[3]    = message_received[3]
            country[4]    = message_received[4]
            country[5]    = message_received[5]
            
            resposta = ('Atualizado com Sucesso!')
            return resposta
        

    resposta = ('Não cadastrado.')
    return resposta
#################################################################################
#################################################################################
def delete(message_received, list_of_countries):
    
    name = message_received[0]

    for country in list_of_countries:
        if name.lower() == country[0].lower():
            list_of_countries.remove(country)
            
            resposta = ('Deletado com Sucesso!')
            return resposta
        
    resposta = ('Não cadastrado.')
    return resposta
#################################################################################
#################################################################################

while op != '5':

    op = socketDados.recv(1).decode()
    
    len_message = int.from_bytes(socketDados.recv(1),'big')
    
    message = socketDados.recv(len_message).decode()
    msg_list = message.split("**")

    # Create
    if op == '1':

        resposta = create(msg_list, countries)
        socketDados.send(len(resposta.encode()).to_bytes(1,'big') + resposta.encode())

    # Read
    elif op == '2':

        resposta = read(msg_list, countries)
        socketDados.send(len(resposta.encode()).to_bytes(1,'big') + resposta.encode())
        
    #Update
    elif op == '3':

        resposta = update(msg_list, countries)
        socketDados.send(len(resposta.encode()).to_bytes(1,'big') + resposta.encode())

    #Delete
    elif op == '4':

        resposta = delete(msg_list, countries)
        socketDados.send(len(resposta.encode()).to_bytes(1,'big') + resposta.encode())

    # se for 5, recebe apenas op e nem faz nada
    # por isso não tem um if dedicado

socketDados.close()
servidorConexao.close()