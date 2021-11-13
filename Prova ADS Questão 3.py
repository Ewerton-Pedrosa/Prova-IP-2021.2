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



print(nota_100)
print(nota_50)
print(nota_20)
print(nota_10)
print(nota_5)
print(nota_2)
print(nota_1)