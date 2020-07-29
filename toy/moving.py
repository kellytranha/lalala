import sys

def main():

    contents = sys.stdin.readlines()
    num_row = int(contents[0].split()[0])
    num_col = int(contents[0].split()[1])
    num_win = int(contents[0].split()[2])

    board = []
    for i in range(1, num_row + 1):
        board.append(contents[i].split())

    def check_row(board, num_row, num_col, num_win):
        for i in range(num_row):
            for j in range(num_col):
                for k in range(num_win):
                    if j + k < num_col and board[i][j] == board[i][j + k] and board[i][j] != "O":
                        color = board[i][j]
                        pass
                    else:
                        break
                else:
                    return color
    
    def check_col(board, num_row, num_col, num_win):
        for i in range(num_row):
            for j in range(num_col):
                for k in range(num_win):
                    if i + k < num_row and board[i][j] == board[i + k][j] and board[i][j] != "O":
                        color = board[i][j]
                        pass
                    else:
                        break
                else:
                    return color
    
    def check_dia(board, num_row, num_col, num_win):
        for i in range(num_row):
            for j in range(num_col):
                for k in range(num_win):
                    if i + k < num_row and j + k < num_col and board[i][j] == board[i + k][j + k] and board[i][j] != "O":
                        color = board[i][j]
                        pass
                    if i + k < num_row and j - k > 0 and board[i][j] == board[i + k][j - k] and board[i][j] != "O":
                        color = board[i][j]
                        pass
                    else:
                        break
                else:
                    return color

                
    if check_row(board, num_row, num_col, num_win) == "R" or check_col(board, num_row, num_col, num_win) == "R" or check_dia(board, num_row, num_col, num_win) == "R":
        print("RED WINS")
    elif check_row(board, num_row, num_col, num_win) == "B" or check_col(board, num_row, num_col, num_win) == "B" or check_dia(board, num_row, num_col, num_win) == "B":
        print("BLUE WINS")
    else:
        print("NONE")


if __name__ == "__main__":
    main()