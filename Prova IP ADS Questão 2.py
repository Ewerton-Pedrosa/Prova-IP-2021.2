candidatos = {}
candidatosList = []
eleitores = []
eleitorVotou = []
votosValidos = []
votosNulos = votosBrancos =0

# INICIA COM O CADASTRO DE CANDIDATOS
print('INICIANDO CADASTRO DE CANDIDATOS // PARA FINALIZAR O CADASTRO DIGITE: FIM')
while True:
    print('=-='*20)
    candidato = input(f'Cadastre o NOME do {len(candidatos)+1}º candidato: ') # não deixar cadastrar vazio
    if candidato.upper() == 'FIM':
        break
    numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
    
    # AFERINDO SE O NÚMERO DIGITADO JÁ PERTENCE A OUTRO CANDIDATO
    if numCandidato in candidatosList or int(numCandidato) < 0:
        while True:
            print('Cadastre um ID ÚNICO e POSITIVO')
            numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
            
            # SAIRÁ DO LOOP SE O NÚMERO DIGITADO NÃO PERTENCER A OUTRO CANDIDATO
            if numCandidato not in candidatosList and int(numCandidato) > 0: 
                break
    candidatosList.append(numCandidato) # Lista auxiliar           
    candidatos[numCandidato] = candidato 
candidatosLock = tuple(candidatos.items()) 
print(candidatosLock)
print(candidatosLock[0][1]) # Achando elemento na tupla dentro da tupla

# CADASTRO DE ELEITORES
print('INICIANDO CADASTRO DE ELEITORES // PARA FINALIZAR O CADASTRO DIGITE: FIM')
while True:
    eleitor = input(f'Cadastre o indentificador do {len(eleitores)+1}º eleitor: ')
    
    # VERIFICA SE ID JÁ FOI CADASTRADO
    if eleitor in eleitores:
        while True:
            print('Identificador DUPLICADO, Favor inserir novo ID!')
            eleitor =  input(f'Cadastre o indentificador do {len(eleitores)+1}º eleitor: ')

            # SE NOVO ID É ÚNICO SAI DO LOOP
            if eleitor not in eleitores:
                break
    if int(eleitor) < 0:
        break
    eleitores.append(eleitor)
eleitoresLock = tuple(eleitores)
print(eleitoresLock)

# INICIO DA VOTAÇÃO
print('-=-'*25)
print('INICIO DA VOTAÇÃO')
print('-=-'*25)
for i in range(len(eleitoresLock)):
    idEleitor = input('Digite o ID do Eleitor: ')
    
    # LOOP QUE VERIFICA SE ELEITOR ESTÁ CADASTRADO
    while True:
        if idEleitor not in eleitoresLock:
            print('ID de Eleitor NÃO CADASTRADO! Insira um ID válido!')
            idEleitor = input('Digite o ID do Eleitor: ')
        elif idEleitor in eleitorVotou:
            
            # LOOP QUE VERIFICA SE ELEITOR JÁ VOTOU
            while True:
                print('Eleitor já votou, insira novo ID de Eleitor!')
                idEleitor = input('Digite o ID do Eleitor: ')
                if idEleitor not in eleitorVotou:
                    break
        else:
            break

    voto = input('Digite o ID do seu candidato: ')
    eleitorVotou.append(idEleitor)

    # VERIFICA EM QUEM O ELEITOR VOTOU
    if voto == '0':
        votosBrancos += 1
    elif voto not in candidatosList:
        votosNulos += 1
    else:
        votosValidos.append(voto)   

print(f'votos válidos {votosValidos}')
print(f'votos nulos: {votosNulos}')
print(f'votos brancos: {votosBrancos}')
