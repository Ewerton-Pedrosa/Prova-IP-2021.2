# Prova ADS 2021.2
# 1ª Questão - Zero ou Um Americano

from time import sleep

soma = subtracao = controle = 0

# Iniciando jogo
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
print(f'Total: {soma}') # Mostra na tela a soma
print(f'O vencedor foi o participante de número {controle}!') # Mostra na tela o vencedor




