class Pilha:
    def __init__(self,tammax):
        self.dados = [0]*tammax
        self.nelems = 0 
    def empilha(self, x):
        if self.nelems == len(self.dados):
            return False
        
        if self.nelems <len(self.dados):
            self.dados[self.nelems] = x
            self.nelems+=1
            return True

        return False
        
    def desempilha(self):
        if len(self.dados)>0:
            self.nelems -=1
            return True, self.dados[self.nelems]
    
        return False, -1
        
    def printa(self):
        print(self.dados)
    


pilha = Pilha(2)
pilha.empilha(2)
pilha.empilha(3)
pilha.printa()
