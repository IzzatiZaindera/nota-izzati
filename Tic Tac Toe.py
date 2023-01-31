board = [' ' for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def is_victory(icon):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combination in win_combinations:
        result = True
        for cell in combination:
            if board[cell] != icon:
                result = False
                break
        if result == True:
            return True
    return False

def main():
    print_board()
    while True:
        player_move('X')
        print_board()
        if is_victory('X'):
            print("X wins! Congratulations!")
            break
        player_move('O')
        print_board()
        if is_victory('O'):
            print("O wins! Congratulations!")
            break

main()
