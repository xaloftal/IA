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
        print("1. matriz 1030")
        print("2. matriz 2530")
        print("3. matriz 5030")
        print("4. matriz 10030")
        print("5. matriz 2530")
        print("6. matriz 5030")
        print("7. Voltar")

        choice_matrices = input("\nEscolha uma opção: ")

        if choice_matrices == '1':
            return matrix1030
        elif choice_matrices == '2':
            return matrix2530
        elif choice_matrices == '3':
            return matrix5030
        elif choice_matrices == '4':
            return matrix10030
        elif choice_matrices == '5':
            return matrix2550
        elif choice_matrices == '6':
            return matrix5050
        elif choice_matrices == '7':
            return None
        else:
            print("Opção inválida. Tente novamente.")

def choose_start(matrix):
    while True:
        start_row = input("\nEscolha a linha do ponto inicial: ")
        start_col = input("Escolha a coluna do ponto inicial: ")

        if (
            not start_row.isdigit()
            or not start_col.isdigit()
            or int(start_row) < 0
            or int(start_col) < 0
            or int(start_row) >= len(matrix)
            or int(start_col) >= len(matrix[0])
        ):
            print("Escolha uma posição válida dentro da matriz.")
            continue

        if matrix[int(start_row)][int(start_col)] == 1:
            print("Escolheu um obstáculo. Escolha outro ponto inicial.")
        else:
            return int(start_row), int(start_col)
          
def choose_end(matrix):
    while True:
        end_row = input("Escolha a linha do objetivo: ")
        end_col = input("Escolha a coluna do objetivo: ")
        print("\n")

        if (
            not end_row.isdigit()
            or not end_col.isdigit()
            or int(end_row) < 0
            or int(end_col) < 0
            or int(end_row) >= len(matrix)
            or int(end_col) >= len(matrix[0])
        ):
                print("Escolha uma posição válida dentro da matriz.")
                continue

        if matrix[int(end_row)][int(end_col)] == 1:
            print("Escolheu um obstáculo. Escolha outro ponto inicial.")
        else:
            return int(end_row), int(end_col)


if __name__ == '__main__':
    while True:
        choice = show_menu()

        #### Benchmark ####
        if choice == '1':
            choice_submenu = show_submenu()

            if choice_submenu == '1':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    bfs_path(matrix, start, end)
                    break

            elif choice_submenu == '2':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    dfs_path(matrix, start, end)
                    break

            elif choice_submenu == '3':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    astar_path(matrix, start, end)
                    break

        #### Visualização gráfica ####
        elif choice == '2':
            choice_submenu = show_submenu()
            if choice_submenu == '1':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    bfs_visualization(matrix, start, end, choice)

            elif choice_submenu == '2':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    dfs_visualization(matrix, start, end, choice)
                    break

            elif choice_submenu == '3':
                matrix = show_menu_matrices()
                if matrix:
                    start = choose_start(matrix)
                    end = choose_end(matrix)
                    astar_visualization(matrix, start, end, choice)
                    break
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")