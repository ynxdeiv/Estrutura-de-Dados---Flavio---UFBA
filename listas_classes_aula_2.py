class Lista:
    def __init__ (self,tammax):
        self.elementosnumero = 4
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
    def remove(self, z):
        if z not in self.dados:
            return True
        for _ in range(self.elementosnumero):
            if self.dados[_] == z:
                self.dados.remove(z)
                self.dados.append(0)
                return True
        return False
    

l = Lista(4)
print(l.insere(10))  # True
print(l.insere(20))  # True
print(l.insere(30))  # True
print(l.insere(40))  # True
print(l.dados)
