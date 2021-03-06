from time import sleep
import emoji

cont = 0
# ---------- CABEÇALHO ----------
print('=-='*25)
print(f'{"BANCO MUNDIAL":^75}')
print('=-='*25)
saque = int(input('Qual o valor do saque R$ '))

# CALCULO QUE DEFINE SAÍDA DAS NOTAS
nota_100 = saque // 100
resto_nota_100 = saque % 100
nota_50 = ( resto_nota_100 // 50)
resto_nota_50 = ( resto_nota_100 % 50)
nota_20 = resto_nota_50 // 20
resto_nota_20 = resto_nota_50 % 20
nota_10 = resto_nota_20 // 10
resto_nota_10 = resto_nota_20 % 10
nota_5 = resto_nota_10 // 5
resto_nota_5 = resto_nota_10 % 5
nota_2 = resto_nota_5 // 2
nota_1 = resto_nota_5 % 2

# INTERAÇÃO COM USUÁRIO USANDO SLEEP PARA SIMULAR RETARDO NO PROCESSAMENTO DO PEDIDO
print('PREPARANDO SEU SAQUE, POR FAVOR AGUARDE', end='')
sleep(0.8)
print(emoji.emojize(":money_with_wings:"), end='')
sleep(0.8)
print(emoji.emojize(":money_with_wings:"), end='')
sleep(0.8)
print(emoji.emojize(":money_with_wings:"))
sleep(0.8)

# MOSTRA NA TELA O RESULTADO DO SAQUE
cedulas = (nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, nota_1)
print('Seu saque terá:')
for i in (100,50,20,10,5,2,1):
    if cedulas[cont] > 0:
        print(f'{cedulas[cont]} cédulas de R${i}', end=' ')
        sleep(0.8)
        print(emoji.emojize(":money_bag:"))
        sleep(0.8)
    cont += 1
