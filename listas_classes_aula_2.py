class Lista:
    def __init__ (self,tammax):
        self.elementosnumero = 0
        self.dados = [0]*tammax

    def consulta(self, x):
        for _ in range(self.elementosnumero):
            if self.dados[_] == x:
                return (True, self.dados[_]) 
        return False
        
    def insere(self, y):
            
        if  self.consulta(y):
            return False

        elif self.elementosnumero<len(self.dados):
            self.dados[self.elementosnumero] = y
            self.elementosnumero+=1
            return True
        return False
    
    def remove(self, z):
        if self.consulta(z):
            ...
            
        # for _ in range(self.elementosnumero):
        #     if self.dados[_]== z:
        #         self.elementosnumero-=1
        #         self.dados[_] = self.dados[self.elementosnumero]
        #         self.dados.pop()
        #         return True
            
        return False
    

l = Lista(5)
l.insere(10)
l.insere(7)
l.insere(3)
l.insere(15)
l.insere(13)
print(l.dados)
l.remove(10)
'''
Casos: 
    1 lista vazia
    2 lista nao vazia
        x ta na lista
        x n ta na lista 
        (corrigir funcaoremove)

        

exercicio: 
    pilhas
    


'''
print(l.dados)