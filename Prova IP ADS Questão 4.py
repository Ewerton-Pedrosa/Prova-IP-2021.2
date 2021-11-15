import math

# DECLARANDO VARIÁVEIS
cont = 1
notas = []
notasAcimaMedia = []
distanciaAteMedia = []

# LOOP DE ENTRADA DE DADOS
while True:
    nota = int(input(f'Digite a nota {cont}: '))
    if nota < 0:
        break
    notas.append(nota)
    cont += 1

# CALCULA NOTAS PARA EXIBIR NA TELA FINAL
media = (sum(notas)/len(notas))
qtNotas = len(notas)
somaNotas = sum(notas)
for i in range(len(notas)):
    if notas[i] > media:
        notasAcimaMedia.append(notas[i])

# CALCULO MANUAL DO DESVIO PADRÃO
for i in range(len(notas)):
    distanciaAteMedia.append(math.pow(notas[i]-media, 2))     # Cria lista com distancias entre elementos e média
somaDistancias = sum(distanciaAteMedia) # Soma todos os elementos da lista "distanciaAteMedia"
somatorioDivQtNotas = somaDistancias/qtNotas # Somatorio dividido pela quantidade de notas
desvioPadrao = math.sqrt(somatorioDivQtNotas) # Uso biblioteca Math para calcular Raiz Quadrada

# EXIBIR RESULTADOS
print(f'Notas na ordem de inserção: {notas}') # Mostra notas na Ordem de entrada
print(qtNotas) # Mostra quantas notas foram inseridas
print(somaNotas) # Mostra a soma das notas
print(media) # Mostra a média das notas
print(notasAcimaMedia) # Lista com notas acima da média
print(desvioPadrao)
