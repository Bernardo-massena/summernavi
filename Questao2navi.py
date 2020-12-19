import math # biblioteca que será usada para as operações matemáticas

vet = []
soma = 0
maximo = -10
posicao = 0 # definindo as variáveis

for i in range (10): #criando o vetor
    if i % 2 == 0: #definindo par e impar
        resultado = 3**i + 7*(math.factorial(i))
        vet.append(resultado) # adicionando o valor no vetor
        soma += resultado 
        if resultado > maximo: 
            maximo = resultado # se o valor for máximo incluir como tal
            posicao = i # e pegar a sua posição

    else: # mesma coisa
        resultado = 2**i + 4*(math.log(i))
        vet.append(resultado)
        soma += resultado
        if resultado > maximo:
            maximo = resultado
            posicao = i 

media = round(soma/10, 2) #definindo a média
print ('A posição é a de número', posicao, 'e a média é', media)
# printando o resultado no terminal