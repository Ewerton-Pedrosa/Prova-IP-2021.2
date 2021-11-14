cont = 1
notas = []

while True:
    nota = int(input(f'Digite a nota {cont}: '))
    if nota < 0:
        break
    notas.append(nota)
    cont += 1

print(f'Notas na ordem de inserção: {notas}') # Mostra notas na Ordem de entrada
print(len(notas)) # Mostra quantas notas foram inseridas
print(sum(notas)) # Mostra a soma das notas
print((sum(notas)/len(notas))) # Mostra a média das notas

  