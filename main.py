from chessPlayer_B2 import *

def main():
    board = get_new_board()

    reset_type();

    board[31] = 15
    print_num_board(board)
    # print(GetPieceLegalMoves(board, 57))
    # print(GetPieceLegalMoves(board, 31))
    # print(len(GetPieceLegalMoves(board, 31)))
    white_pos = (GetPlayerPositions(board, 10))

    tree_next = []

    for i in white_pos:
        tree_next += [GetPieceLegalMoves(board, i)]

    board_next = next_board(board, [1]) # move is of the form [position 1, position 2]

    print("l")

    print_num_board(board)

    print(tree_next)

main()
