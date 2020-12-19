x = 3626 #menor número que satisfaz as condições do problema
multiplos = 0

while x <= 5000000 : # impondo o limite de 5 milhões
    if x % 49 == 0 and x % 37 == 0 :
        multiplos += 1 
    x += 2 # indo de par em par
print('A quantidade de múltiplos de 2, 49 e 37 é', multiplos)
# printando a resposta