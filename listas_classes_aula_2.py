class Lista:
    def __init__ (self,tammax):
        self.elementosnumero = 0
        self.dados = [0]*tammax

    def consulta(self, x):
        for _ in range(self.elementosnumero):
            if self.dados[_] == x:
                return True
        return False
        
    def insere(self, y):
            
        if  self.consulta(y):
            return True

        elif self.elementosnumero<len(self.dados):
            self.dados[self.elementosnumero] = y
            self.elementosnumero+=1
            return True
        
        else:
            return False
