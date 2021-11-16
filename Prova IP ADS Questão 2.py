candidatos = {}
candidatosList = []

# INICIA COM O CADASTRO DE CANDIDATOS
print('INICIANDO CADASTRO DE CANDIDATOS // PARA FINALIZAR O CADASTRO DIGITE: FIM')
while True:
    print('=-='*20)
    candidato = input('Digite o nome do candidato: ')
    if candidato.upper() == 'FIM':
        break
    numCandidato =  input('Digite o número do candidato: ')
    
    # AFERINDO SE O NÚMERO DIGITADO JÁ PERTENCE A OUTRO CANDIDATO
    if numCandidato in candidatosList:
        while True:
            print('O número informado já pertence a outro candidato, digite um número válido!')
            numCandidato =  input('Digite o número do candidato: ')
            
            # SAIRÁ DO LOOP SE O NÚMERO DIGITADO NÃO PERTENCER A OUTRO CANDIDATO
            if numCandidato not in candidatosList: 
                break
    candidatosList.append(numCandidato) # Lista aux. para aferir se candidatos tem números iguais           
    candidatos[numCandidato] = candidato 
print(candidatos)

# CADASTRO DE ELEITORES
