#abrem o anaconda powershell e depois colem isto:  conda init powershell
class NoArvore: #esta classe representa a arvore; um no individual da arvore
    def __init__(self, valor): 
      self.valor = valor 
      self.filhos = [] #numero de filhos
      self.pai = None

    def adicionar_filho(self, filho): #adicionar um filho ao objeto self, tornando o self o pai
        filho.pai = self
        self.filhos.append(filho)

    def procurar_nivel(self): #conta se o numero de antepassados (pais anteriores)
        nivel = 0 #o no raiz esta no nivel 0
        p = self.pai
        while p: #enquanto existir pai incrementa-se um nivel
           nivel += 1 
           p = p.pai
        return nivel

    def mostrar_arvore(self): #funcao para imprimir a arvore
      espacos = ' ' * self.procurar_nivel()  #isto inicializa um espaco a cada nivel; nivel 1 com 1 espaco, 2 com 2 e etc..
      ramo = espacos + "|_" if self.pai else "" #se existir pai
      print(ramo + str(self.valor)) #imprime o pai
      if len(self.filhos) > 0: #se houver filhos
        for filho in self.filhos:
            filho.mostrar_arvore() #imprime os valores dos seguintes filhos


def construir_arvore():
    raiz = NoArvore(1)

    laptop = NoArvore(2)
    laptop.adicionar_filho(NoArvore("Mac"))
    laptop.adicionar_filho(NoArvore("Surface"))
    laptop.adicionar_filho(NoArvore("Thinkpad"))

    cellphone = NoArvore("Cell Phone")
    cellphone.adicionar_filho(NoArvore("iPhone"))
    cellphone.adicionar_filho(NoArvore("Google Pixel"))
    cellphone.adicionar_filho(NoArvore("Vivo"))

    tv = NoArvore("TV")
    tv.adicionar_filho(NoArvore("Samsung"))
    tv.adicionar_filho(NoArvore("LG"))

    raiz.adicionar_filho(laptop)
    raiz.adicionar_filho(cellphone)
    raiz.adicionar_filho(tv)

    raiz.mostrar_arvore()

if __name__ == '__main__':
    construir_arvore()

