candidatos = {}
candidatosList = []
eleitores = []

# INICIA COM O CADASTRO DE CANDIDATOS
print('INICIANDO CADASTRO DE CANDIDATOS // PARA FINALIZAR O CADASTRO DIGITE: FIM')
while True:
    print('=-='*20)
    candidato = input(f'Cadastre o NOME do {len(candidatos)+1}º candidato: ')
    if candidato.upper() == 'FIM':
        break
    numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
    
    # AFERINDO SE O NÚMERO DIGITADO JÁ PERTENCE A OUTRO CANDIDATO
    if numCandidato in candidatosList:
        while True:
            print('O número informado já pertence a outro candidato, digite um número válido!')
            numCandidato =  input(f'Cadastre o ID do {len(candidatos)+1}º candidato: ')
            
            # SAIRÁ DO LOOP SE O NÚMERO DIGITADO NÃO PERTENCER A OUTRO CANDIDATO
            if numCandidato not in candidatosList: 
                break
    candidatosList.append(numCandidato) # Lista aux. para aferir se candidatos tem números iguais           
    candidatos[numCandidato] = candidato 
print(candidatos) # Falta converter a lista candidatos em uma tupla qd finalizar o cadastro.

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
print(eleitores)
 