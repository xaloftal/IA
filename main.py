from fixedMatrices import *
from bfs import *
from dfs import *
from aStar import astar_path

def show_menu():
    print("MENU:")
    print("1. Benchmark")
    print("2. Visualização gráfica")
    print("3. Sair")

    choice_menu = input("\nEscolha uma opção: ")

    return choice_menu

def show_submenu():
    print("MENU:")
    print("1. Algoritmo de pesquisa em largura")
    print("2. Algoritmo de pesquisa em profundidade")
    print("3. A estrela")
    print("4. Voltar")

    choice_submenu = input("\nEscolha uma opção: ")

    return choice_submenu
    
def show_menu_matrices():
    print("MENU:")
    print("1. matriz 2530")
    print("2. matriz 1010")
    print("3. Voltar")

    choice_matrices = input("\nEscolha uma opção: ")

    while True:
        if choice_matrices == '1':
            matrix = matrix2530
        elif choice_matrices == '2':
            matrix = matrix1030
        elif choice_matrices == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    return matrix

def choose_start():
    start_row = input("\nEscolha a linha do ponto incial: ")
    start_col = input("\nEscolha a coluna do ponto incial: ")

    return (start_row, start_col)

def choose_goal():
    goal_row = input("\nEscolha a linha do objetivo: ")
    goal_col = input("\nEscolha a coluna do objetivo: ")

    return (goal_row, goal_col)

if __name__ == '__main__':
    while True:
        choice = show_menu()

        ####Benchmark####
        if choice == '1':
           choice_submenu = show_submenu()

           if choice_submenu == '1':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
                bfs_path(matrix, start, goal)

           elif choice_submenu == '2':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
                dfs_path(matrix, start, goal)

           elif choice_submenu == '3':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
                astar_path(matrix, start, goal)
           else: 
            print("Opção inválida. Tente novamente.")

        ####Visualização gráfica####

        elif choice == '2':
            choice_submenu = show_submenu()
            if choice_submenu == '1':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
            elif choice_submenu == '2':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
            elif choice_submenu == '3':
                matrix = show_menu_matrices()
                start = choose_start()
                goal = choose_goal()
            else: 
                print("Opção inválida. Tente novamente.")

        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")


    


