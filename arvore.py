class TreeNode: #this class represents the tree, por nodes
  def __init__(self, data):
    self.data = data #what data you want to represent
    self.children = [] #instancias da tree node class
    self.parent = None
  
  #metodo para adicionar filhos
  def add_child(self, child): 
    child.parent = self #o self vai se tornar o parent do child
    self.children.append(child) 

  #tells the level of the node
  def get_level(self): 
    #count number of parents/ancestors
    level = 0
    p = self.parent
    while p: #enquanto existe um parente (enquanto não é root). visto por exemplo da folha para a root. vai do fundo para cima
      level += 1
      p = p.parent
    return level  

  #metodo para mostrar os dados
  def print_tree(self):
    spaces = ' ' * self.get_level() * 3 #adiciona 3 espaços a cada nivel
    prefix = spaces + "|__" if self.parent else "" #usa outros caracteres para mostrar a hierarquia mais facilmente. se for root, nao poe nada

    print(prefix + self.data) 
    #agora quero dar print aos filhos
    if self.children: #self.children > 0
      for child in self.children:
        child.print_tree() #enquanto tiver filhos, vai sendo recursiva. quando for leaf node, não chama de volta sozinho.



#
#
# EXEMPLO DE ARVORE
#
#

#construir uma arvore
def build_product_tree():
  root = TreeNode("Electronics")

  #laptop e os filhos
  laptop = TreeNode("Laptop")
  laptop.add_child(TreeNode("Mac")) #cada child é uma instância de TreeNode
  laptop.add_child(TreeNode("Surface"))
  laptop.add_child(TreeNode("Thinkpad"))

  #cellphone e os seus filhos
  cellphone = TreeNode("Cell phone")
  cellphone.add_child(TreeNode("iPhone")) 
  cellphone.add_child(TreeNode("Google Pixel")) 
  cellphone.add_child(TreeNode("Vivo"))   

  #tv e os seus filhos
  tv = TreeNode("TV")
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))

  #filhos de eletronics
  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)

  return root

if __name__ == '__main__':
  root = build_product_tree()
  root.print_tree()
  pass