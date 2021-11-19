import math

# DECLARANDO VARIÁVEIS
cont = 1
notas = []
notasAcimaMedia = []
distanciaAteMedia = []
# CABEÇALHO
print('-=-'*25)
print(f'{"CÁLCULO DE NOTAS":^75}')
print('-=-'*25)
# LOOP DE ENTRADA DE DADOS
while True:
    nota = int(input(f'Digite a nota {cont}: '))
    if 0 <= nota <= 10:
        notas.append(nota)
        cont += 1
    elif nota > 10:
        print('ERRO: INSIRA UMA NOTA ENTRE 0 E 10!')
    elif nota < 0:
        break
    

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
print('-=-'*25)
print(f'{"RESULTADO FINAL":^75}')
print('-=-'*25)
print(f'Notas na ordem de inserção: {notas}') # Mostra notas na Ordem de entrada
print(f'Foram inseridas {qtNotas} notas') # Mostra quantas notas foram inseridas
print(f'A soma das notas é igual a {somaNotas}') # Mostra a soma das notas
print(f'A média das notas é {media}') # Mostra a média das notas
print(f'Essas {len(notasAcimaMedia)} notas: {notasAcimaMedia} são as notas acima da média') # Lista com notas acima da média
print(f'O desvio padrão das notas informadas é {desvioPadrao}')
