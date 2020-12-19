n1 = n2 = n3 = n4 = n5 = ''
while n1 is not float: # impedindo de colocar notas não numéricas
    try:
        n1 = float(input('Insira a nota do aluno 1: '))
        break
    except ValueError:
        print('Por favor, insira uma nota válida: ')

while n2 is not float:
    try:
        n2 = float(input('Insira a nota do aluno 2: '))
        break
    except ValueError:
        print('Por favor, insira uma nota válida: ')

while n3 is not float:
    try:
        n3 = float(input('Insira a nota do aluno 3: '))
        break
    except ValueError:
        print('Por favor, insira uma nota válida: ')

while n4 is not float:
    try:
        n4 = float(input('Insira a nota do aluno 4: '))
        break
    except ValueError:
        print('Por favor, insira uma nota válida: ')
        
while n5 is not float:
    try:
        n5 = float(input('Insira a nota do aluno 5: '))
        break
    except ValueError:
        print('Por favor, insira uma nota válida: ')

notas = { #colocando as notas
    'aluno 1': n1,
    'aluno 2': n2,
    'aluno 3': n3,
    'aluno 4': n4,
    'aluno 5': n5,
}

maximo = max(notas.values())

print('O aluno com a maior nota foi o ', [k for k, v in notas.items() if v == maximo], ', que foi: ', maximo)
 #printando os resultados de modo que seja possível colocar mais de um aluno com nota máxima