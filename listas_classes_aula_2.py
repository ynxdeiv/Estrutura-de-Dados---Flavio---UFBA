class Lista:
    def __init__ (self,tammax):
        self.elementosnumero = 0
        self.dados = [0]*tammax

    def consulta(self, x):
        for _ in range(self.elementosnumero):
            if self.dados[_] == x:
                return True
        return False

