# Prova ADS 2021.2
# 1ª Questão - Zero ou Um Americano

from time import sleep

soma = subtracao = controle = 0

# Iniciando jogo
print('-=-'*25)
print(f'{"JOGO ZERO OU UM AMERICANO":^75}')
print('-=-'*25)
while True:
    quantidadeJogadores = int(input('Qual o número de participantes? '))
    if quantidadeJogadores > 1: # Verifica validade da quantidade de participantes
        break
    print('Quantidade de participantes inválida. Digite um valor maior que 1!') 
for player in range(quantidadeJogadores):
    while True:
        numJogador = int(input(f'Numeração do participante {player+1}: '))
        if 0 <= numJogador <= 10: # Verifica validade da quantidade de dedos dos participantes
            soma += numJogador
            break
        print('Número Inválido! Digite um número entre 0 e 10!')
controle = soma

# Lógica matemática para determinar o jogador vencedor
while True:
    controle -= quantidadeJogadores
    if controle <= 0:
        controle += quantidadeJogadores
        break

# Resultado Final
print('-=-'*25)
print('SOMANDO OS DEDOS', end='')
sleep(0.8)
print('.', end='')
sleep(0.8)
print('.', end='')
sleep(0.8)
print('.')
sleep(0.8)
print('-=-'*25)
print(f'O TOTAL de dedos é {soma}') # Mostra na tela a soma
sleep(0.8)
print(f'O VENCEDOR foi o participante de NÚMERO {controle}!') # Mostra na tela o vencedor
