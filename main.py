from chessPlayer_B2 import *

def main():
    board = get_new_board()

    # print_num_board(board)
    # board = get_human_move(10, board);
    # print_num_board(board)
    # board = get_human_move(20, board);
    # print_num_board(board)
    # board = get_human_move(10, board);

    reset_type();

    board[28] = 13
    print_num_board(board)
    # print(GetPieceLegalMoves(board, 57))
    print(GetPieceLegalMoves(board, 28))


main()
