from fixedMatrices import *
from bfs import *
from dfs import *
from aStar import *

def show_menu():
    print("\n\nMENU:")
    print("1. Benchmark")
    print("2. Visualização gráfica")
    print("3. Sair")

    choice_menu = input("\nEscolha uma opção: ")

    return choice_menu

def show_submenu():
    print("\n\nAlgoritmo:")
    print("1. Algoritmo de pesquisa em largura")
    print("2. Algoritmo de pesquisa em profundidade")
    print("3. A estrela")
    print("4. Voltar")

    choice_submenu = input("\nEscolha uma opção: ")

    return choice_submenu
    
def show_menu_matrices():
    while True:
        print("\n\nMatriz:")
        print("1. matriz 2530")
        print("2. matriz 1010")
        print("3. matriz 5030")
        print("4. Voltar")

        choice_matrices = input("\nEscolha uma opção: ")

        if choice_matrices == '1':
            return matrix2530
        elif choice_matrices == '2':
            return matrix1030
        elif choice_matrices == '3':
            return matrix5030
        elif choice_matrices == '4':
            return None
        else:
            print("Opção inválida. Tente novamente.")

def choose_start():
    start_row = input("\nEscolha a linha do ponto inicial: ")
    start_col = input("Escolha a coluna do ponto inicial: ")

    return (int(start_row), int(start_col))
          

def choose_end():
    end_row = input("Escolha a linha do objetivo: ")
    end_col = input("Escolha a coluna do objetivo: ")
    print("\n")

    return (int(end_row), int(end_col))

if __name__ == '__main__':
    while True:
        choice = show_menu()

        #### Benchmark ####
        if choice == '1':
            choice_submenu = show_submenu()

            if choice_submenu == '1':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    bfs_path(matrix, start, end)
                    break

            elif choice_submenu == '2':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    dfs_path(matrix, start, end)
                    break

            elif choice_submenu == '3':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    astar_path(matrix, start, end)
                    break

        #### Visualização gráfica ####
        elif choice == '2':
            choice_submenu = show_submenu()
            if choice_submenu == '1':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    bfs_visualization(matrix, start, end, choice)

            elif choice_submenu == '2':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    dfs_visualization(matrix, start, end, choice)
                    break

            elif choice_submenu == '3':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start()
                    end = choose_end()
                    astar_visualization(matrix, start, end, choice)
                    break
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")