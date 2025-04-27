'''
o mini teste teve duas questões uma para encontrar a quantidade de números maiores que uma chave e outra pra trocar o menor valor pelo ultimo indice 
'''

class Lista:
    def __init__(self, tammax):
        self.dados = [0]*tammax
        self.nelems=0
    def encontraMaior(self,x):

        maiores = 0 
        maior = self.dados[x]

        if self.nelems==0:
            return False, -1

        for _ in range(self.nelems):

            if self.dados[_]>maior:

                maior = self.dados[_]
                maiores+=1
        return True, maiores

        

