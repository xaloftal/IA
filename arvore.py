#abrem o anaconda powershell e depois colem isto:  conda init powershell

class NoArvore: #esta classe representa o primeiro no
    def __init__(self, valor): #a funcao __init__ serve para iniciar classes e dar valores àS propriedades de um objeto (self)
        self.esquerda = None
        self.direita = None
        self.valor = valor

#arvore = NoArvore(2)
#arvore.esquerda = NoArvore(3)
#arvore.direita = NoArvore(1)
#arvore.direita.direita = NoArvore(7)

#a funcao aseguir e a versao automatizada do codigo 4 linhas anteriores

    def inserir(self, valor): #se o novo no tiver um valor menor que o valor anterior vai para a esquerda, e se for maior vai para a direita
        if valor < self.valor:
             if self.esquerda is None:
                  self.esquerda = NoArvore(valor)
             else:
                  self.esquerda.inserir(valor)
        else:
             if self.direita is None:
                  self.direita = NoArvore(valor)
             else:
                  self.direita.inserir(valor)



    #podemos percorrer uma arvore por 3 formas: pre-ordem, em ordem, e pos-ordem; o em ordem e mais adequado 

    def travessia_em_ordem(self): #imprime primeiro o no que se encontra mais a esquerda e depois percorre os anteriores e imprime o que se encontra mais a esquerda primeiro; se nao entenderem depois explico vos melhor
         if self.esquerda:
            self.esquerda.travessia_em_ordem()
         print(self.valor)
         if self.direita:
            self.direita.travessia_em_ordem()
     








  #def add_child(self, child): #adicionar um child ao objeto self, tornando o self o parent
        #child.parent = self
        #self.children.append(child)

arvore = NoArvore(10)
arvore.inserir(4)
arvore.inserir(2)
arvore.inserir(9)
arvore.inserir(6)
arvore.inserir(3)
arvore.inserir(45)
arvore.inserir(56)

arvore.travessia_em_ordem()
