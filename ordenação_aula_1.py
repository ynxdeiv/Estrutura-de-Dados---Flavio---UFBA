"""
Na primeira aula o professor Flavio ensinou
ordenação por inserção

"""

import os

n = int(input('Digite o valor de n: '))
os.system('cls')
vetor = list(map(int,input('Digite os números: ').split()))

for j in range (1, n):
    
    chave = vetor[j]

    i = j-1
    ...
    while (i>=0) and vetor[i] > chave:

        vetor[i+1] = vetor[i]
        i-=1
        ...
    vetor[i+1] = chave
print(vetor)