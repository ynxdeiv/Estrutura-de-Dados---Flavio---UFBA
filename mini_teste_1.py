'''def retornaMaior(self)

    Se a lista não estiver vazia, retorna True e o maior valor de chave armazenada na lista. Se a lista estiver vazia, retorna False e -1.

-----------------------------------

 def retira_i(self): 
    retira o i-ésimo elemento da lista, se houver. Considere que o primeiro elemento da lista possui índice zero e que i < maxtam.




'''


class Lista: 
    def __init__(self, tammax):
        self.lista = []

    def retornaMaior(self):

        if self.lista:
            maior = max(self.lista)
            return True, maior
        else:
            return False, -1
    def retira_i(self, i):
        if 0<=i < len(self.lista) :
            self.lista.pop(i)
            return True
        else:
            return False

...
