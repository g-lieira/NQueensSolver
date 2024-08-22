import time  # Importa o módulo time para medir o tempo de execução do código
import threading  # Importa o módulo threading para criar e gerenciar threads

# Função para verificar se uma rainha pode ser colocada na posição (row, col)
def is_safe(board, row, col):
    # Verifica todas as linhas acima da linha atual
    for i in range(row):
        # Verifica se há outra rainha na mesma coluna ou na diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False  # Retorna False se a posição não for segura
    return True  # Retorna True se a posição for segura

# Função para tentar colocar rainhas em um tabuleiro
def solve_n_queens_thread(board, row, n, solutions, lock):
    if row == n:
        # Se todas as rainhas foram colocadas (row == n), adicione a solução à lista
        with lock:  # Usa um lock para evitar problemas de concorrência ao acessar a lista solutions
            solutions.append(board.copy())  # Adiciona uma cópia do tabuleiro atual à lista de soluções
        return  # Retorna para parar a execução dessa instância da função

    for col in range(n):
        # Tenta colocar uma rainha na posição (row, col)
        if is_safe(board, row, col):  # Verifica se é seguro colocar uma rainha na posição (row, col)
            board[row] = col  # Coloca a rainha na coluna col da linha row
            solve_n_queens_thread(board, row + 1, n, solutions, lock)  # Tenta colocar a próxima rainha
            board[row] = -1  # Remove a rainha da linha row para testar outras possibilidades

# Função para imprimir o tabuleiro
def print_board(board, n):
    for row in range(n):
        # Cria uma linha com '.' em todas as posições
        print(" ".join("Q" if col == board[row] else "." for col in range(n)))  # Substitui '.' pela 'Q' onde há uma rainha
    print("\n")  # Adiciona uma linha em branco após cada tabuleiro

# Função para resolver o problema das N rainhas
def solve_n_queens(n):
    solutions = []  # Lista para armazenar todas as soluções encontradas
    threads = []  # Lista para armazenar todas as threads criadas
    lock = threading.Lock()  # Cria um lock para sincronizar o acesso à lista de soluções
    start_time = time.time()  # Marca o início do tempo de execução

    # Cria e inicia uma thread para cada coluna na primeira linha
    for col in range(n):
        board = [-1] * n  # Cada thread recebe seu próprio tabuleiro inicializado com -1 (nenhuma rainha colocada)
        board[0] = col  # Coloca uma rainha na primeira linha e na coluna atual
        # Cria uma nova thread que executa a função solve_n_queens_thread
        thread = threading.Thread(target=solve_n_queens_thread, args=(board, 1, n, solutions, lock))
        threads.append(thread)  # Adiciona a thread à lista de threads
        thread.start()  # Inicia a thread

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()  # Espera que a thread termine sua execução

    # Imprime todas as soluções encontradas
    for solution in solutions:
        print_board(solution, n)  # Imprime cada solução armazenada na lista solutions

    end_time = time.time()  # Marca o fim do tempo de execução
    print(f"Paralelo: {n}x{n}")  # Imprime o tamanho do tabuleiro
    print(f"Total de soluções encontradas: {len(solutions)}")  # Imprime o número total de soluções encontradas
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos\n")  # Imprime o tempo total de execução
    print("-" * 40)  # Imprime uma linha separadora

# Exemplo de uso
n = 12  # Tamanho do tabuleiro (n x n)
solve_n_queens(n)  # Chama a função para resolver o problema das N rainhas para o tabuleiro de tamanho n
