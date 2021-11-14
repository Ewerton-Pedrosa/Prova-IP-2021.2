cont = 1
notas = []

while True:
    nota = int(input(f'Digite a nota {cont}: '))
    if nota < 0:
        break
    notas.append(nota)
    cont += 1

print(notas)
print(len(notas))
print(sum(notas))
print((sum(notas)/len(notas)))
  