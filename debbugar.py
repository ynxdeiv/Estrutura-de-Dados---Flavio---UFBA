class Lista:
    def __init__ (self,tammax):
    
        self.dados = [0]*tammax
        self.nelems=0
    def retornaMaior(self):
        self.maior = self.dados[0] 
        if self.nelems == 0:
            return False, -1
        for _ in range(self.nelems):
            if self.dados[_]>self.maior:
                self.maior = self.dados[_]
        return True, self.maior
            
    def retirar(self, i):
        if self.nelems == 0:
            return False, -1
        if 0<=i<self.nelems:
            retirado = self.dados.pop(i)
            self.nelems -=1
            return True, retirado
        
    def insere(self, x):     
        if self.nelems<len(self.dados):
            self.dados[self.nelems] = x
            self.nelems+=1
            return True
        return False
    def printa(self):
        print(self.dados)
teste = Lista(4)
teste.insere(1)
teste.insere(4)
teste.insere(3)
teste.insere(2)
teste.printa()
teste.retirar(9)
teste.printa()
teste.retirar(0)
teste.printa()