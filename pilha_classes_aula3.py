class Pilha:
    def __init__(self,tammax):
        self.dados = []
        self.tammax = tammax
        pass

    def empilha(self, x):
        if len(self.dados) <self.tammax:
            self.dados.append(x)
            return True
        else:
            return False
    def desempilha(self):
        if self.dados:
            last = self.dados.pop()
            return True, last
    
        else:
            return False, -1

    '''
        retorna True, valor desempilhado
    '''
    def printa(self):
        print(self.dados)
    


pilha = Pilha(5)
pilha.empilha(2)
pilha.empilha(3)
pilha.printa()
pilha.printa()
