import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minmax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i, j in get_empty_cells(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = 'O'
            eval = minmax(new_board, depth+1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_empty_cells(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = 'X'
            eval = minmax(new_board, depth+1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def ai_move(board):
    best_move = None
    best_eval = float("-inf")
    for i, j in get_empty_cells(board):
        new_board = copy.deepcopy(board)
        new_board[i][j] = 'O'
        eval = minmax(new_board, 0, False)
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        human_move = input("Enter your move (row col): ")
        i, j = map(int, human_move.split())
        board[i][j] = 'X'
        print_board(board)
        
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        ai_move_i, ai_move_j = ai_move(board)
        board[ai_move_i][ai_move_j] = 'O'
        print(f"AI placed O at: {ai_move_i} {ai_move_j}")
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
