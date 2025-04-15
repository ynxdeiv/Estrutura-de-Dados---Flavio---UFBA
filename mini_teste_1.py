'''def retornaMaior(self)
Se a lista não estiver vazia, retorna True e o maior valor de chave armazenada na lista. Se a lista estiver vazia, retorna False e -1.'''

class Lista: 
    def __init__(self):
        self.lista = [1,2,3,4,5,6,7,8]
        self.tamanhomax=10

    def retornaMaior(self):

        if self.lista:
            maior = max(self.lista)
            return True, maior
        else:
            return False, -1

    
