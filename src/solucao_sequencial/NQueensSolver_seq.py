import time  # Importa o módulo time para medir o tempo de execução do código

def print_board(board):
    # Imprime o tabuleiro
    n = len(board)  # Obtém o tamanho do tabuleiro (n x n)
    for row in range(n):
        # Cria uma linha com '.' em todas as posições
        line = ['.' for _ in range(n)]
        # Substitui '.' por 'Q' na coluna onde a rainha está colocada
        line[board[row]] = 'Q'
        # Imprime a linha atual do tabuleiro
        print(" ".join(line))
    print()  # Adiciona uma linha em branco após cada tabuleiro

def is_safe(board, row, col):
    # Verifica se é seguro colocar uma rainha na posição (row, col)
    for i in range(row):
        # Verifica se há outra rainha na mesma coluna ou na diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False  # Retorna False se a posição não for segura
    return True  # Retorna True se a posição for segura

def solve_n_queens(n):
    # Resolve o problema das N rainhas e retorna todas as soluções possíveis
    def solve(row):
        # Verifica se todas as rainhas foram colocadas (row == n)
        if row == n:
            # Adiciona uma cópia do tabuleiro atual à lista de soluções
            solutions.append(board.copy())
            return
        for col in range(n):
            # Tenta colocar uma rainha na posição (row, col)
            if is_safe(board, row, col):  # Verifica se é seguro colocar uma rainha na posição (row, col)
                board[row] = col  # Coloca a rainha na coluna col da linha row
                solve(row + 1)  # Tenta colocar a próxima rainha na próxima linha
                board[row] = -1  # Remove a rainha da linha row para testar outras possibilidades

    board = [-1] * n  # Inicializa o tabuleiro com -1 (nenhuma rainha colocada)
    solutions = []  # Lista para armazenar todas as soluções encontradas
    solve(0)  # Inicia a solução a partir da primeira linha (linha 0)
    return solutions  # Retorna todas as soluções encontradas

def main(n):
    start_time = time.time()  # Marca o início do tempo de execução
    solutions = solve_n_queens(n)  # Chama a função para resolver o problema das N rainhas
    end_time = time.time()  # Marca o fim do tempo de execução
    
    for solution in solutions:
        print_board(solution)  # Imprime cada solução armazenada na lista solutions
        
    print(f"Sequencial: {n}x{n}:")  # Imprime o tamanho do tabuleiro
    print(f"Total de soluções encontradas: {len(solutions)}")  # Imprime o número total de soluções encontradas
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")  # Imprime o tempo total de execução
    print("-" * 40)  # Imprime uma linha separadora

# Exemplo de uso
if __name__ == "__main__":
    n = 12  # Define o tamanho do tabuleiro (n x n)
    main(n)  # Chama a função principal para resolver o problema das N rainhas para o valor de n definido
