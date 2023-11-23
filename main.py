import randomMatrices
import fixedMatrices
import bfs
import dfs
import aStar

def show_menu():
    print("MENU:")
    print("1. What type of matrix do you want?")
    print("2. Which search algorithm do you want to try?")
    print("3. Exit")

def get_size(dimensao):
    return int(input("Enter the {dimensao} of matrix: "))
  
def choice1():
    matrix_type = input("\n1.Random\n2.Fixed\nChoose matrix type: ")
    
    if matrix_type == '1':
        size = get_size()
        matrix = randomMatrices()
        return matrix
    elif matrix_type == '2':
        size = get_size()
        matrix = fixedMatrices()
        return matrix
    else:
        print("Invalid choice for matrix type.")  
        return None      

def choice2():
    algorithm_search = input("1.bfs\n2.dfs\n3.aStar\nChoose algorithm search: ")
    if algorithm_search == '1':
        search = bfs()
        return search
    elif algorithm_search == '2':
        search = dfs()
        return search
    elif algorithm_search == '3':
        search = aStar()
        return search
    else:
        print("Invalid choice for matrix type.")  
        return None    
               
# def opcao3():
#     print("Você escolheu a Opção 3.")

# Loop principal
while True:
    show_menu()

    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        choice1()
    elif escolha == '2':
        choice2()
        
    # elif escolha == '3':
        
    # elif escolha == '4':
    #     print("Saindo do programa.")
    #     break
    else:
        print("Opção inválida. Tente novamente.")
