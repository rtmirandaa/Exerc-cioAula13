class pilha:
    def __init__(self):
        self.topo = None    
        self.tamanho = 0
        
    def add(self, livro):
        novo_no = livro
        if self.topo is None:
            self.topo = novo_no
        else:
            novo_no.proximo = self.topo
            self.topo = novo_no
        self.tamanho += 1
        return self
    
    def remover(self):
        if self.topo is None:
            return None
        else:
            aux = self.topo
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return aux
    
    def imprimir(self):
        atual = self.topo
        while atual:
            print(atual.titulo)
            atual = atual.proximo
