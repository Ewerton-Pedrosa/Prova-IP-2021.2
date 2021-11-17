candidatos = {}
candidatosList = []
eleitores = []
eleitorVotou = []
votosValidos = []
contagemDeVotos = []
votosNulos = votosBrancos = 0


# ------------INICIA COM O CADASTRO DE CANDIDATOS------------
print('INICIANDO CADASTRO DE CANDIDATOS // PARA FINALIZAR O CADASTRO DIGITE: FIM')
while True:
    print('=-='*25)
    candidato = input(f'Cadastre o NOME do {len(candidatos)+1}º candidato: ').strip().upper() # não deixar cadastrar vazio
    if candidato == 'FIM':
        break
    elif candidato == '':
        while True:
            print('ERRO!! Você precisa cadastrar uma NOME para o CANDIDATO!')
            candidato = input(f'Cadastre o NOME do {len(candidatos)+1}º candidato: ').strip().upper()
            if candidato != '':
                break
    numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
    
    # AFERINDO SE O NÚMERO DIGITADO JÁ PERTENCE A OUTRO CANDIDATO
    if numCandidato in candidatosList or int(numCandidato) < 0:
        while True:
            print('ERRO! Cadastre um ID ÚNICO e POSITIVO')
            numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
            
            # SAIRÁ DO LOOP SE O NÚMERO DIGITADO NÃO PERTENCER A OUTRO CANDIDATO
            if numCandidato not in candidatosList and int(numCandidato) > 0: 
                break
    candidatosList.append(numCandidato) # Lista auxiliar           
    candidatos[numCandidato] = candidato 
candidatosLock = tuple(candidatos.items()) # Transforma em tupla para não haver mais edições

# ------------CADASTRO DE ELEITORES------------
print('=-='*25)
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
    if eleitor.upper() == 'FIM':
        break
    eleitores.append(eleitor)
eleitoresLock = tuple(eleitores) #Transforma em Tupla para não haver mais edições

# ------------INICIO DA VOTAÇÃO------------
print('-=-'*25)
print(f'{"INICIO DA VOTAÇÃO":^75}')
print('-=-'*25)
for i in range(len(eleitoresLock)):
    idEleitor = input(f'Digite o ID do {i+1}º Eleitor: ')
    
    # LOOP QUE VERIFICA SE ELEITOR ESTÁ CADASTRADO
    while True:
        if idEleitor not in eleitoresLock:
            print('ID de Eleitor NÃO CADASTRADO! Insira um ID válido!')
            idEleitor = input(f'Digite o ID do {i+1}º Eleitor: ')
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

# ------------ APURAÇÃO DOS VOTOS // RESULTADO FINAL ------------
# CRIO LISTA COM QUANTIDADE DE VOTOS POR CANDIDATO
for i in range(len(candidatosList)):
    contagemDeVotos.append(votosValidos.count(candidatosList[i]))
maisVotos = max(contagemDeVotos, key=int)
posicaoMaisVotado = contagemDeVotos.index(maisVotos)
percentualGanhador = (contagemDeVotos[posicaoMaisVotado]/sum(contagemDeVotos))*100

# ------------ PRINTS DE RESULTADOS FINAIS ------------
print('-=-'*25)
print(f'{"RESULTADO FINAL":^75}')
print('-=-'*25)
print(f'\nO VENCEDOR da votação foi {candidatosLock[posicaoMaisVotado][1]} com {percentualGanhador:.2f}% dos votos válidos!', end='\n\n')
for i in range(len(candidatosList)):
    print(f'O candidato {candidatosLock[i][1]} teve {contagemDeVotos[i]} votos!')
print(f'\nVOTOS NULOS: {votosNulos}')
print(f'\nVOTOS EM BRANCO: {votosBrancos}')
