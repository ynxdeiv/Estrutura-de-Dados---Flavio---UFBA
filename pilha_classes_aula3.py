class Pilha:
    def __init__(self,tammax):
        self.dados = []
        self.tammax = tammax
        self.nelems = 0 
    def empilha(self, x):
        if self.nelems <len(self.dados):
            self.dados[self.nelems] = x

            return True

        return False
        
    def desempilha(self):
        if self.dados:
            last = self.dados.pop()
            return True, last
    
        return False, -1
        
    def printa(self):
        print(self.dados)
    


pilha = Pilha(5)
pilha.empilha(2)
pilha.empilha(3)
pilha.printa()
pilha.printa()
