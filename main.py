from chessPlayer_trees import *

def main():
    # board = get_new_board()
    #
    # reset_type();
    #
    # board[31] = 15
    # print_num_board(board)
    #
    # white_pos = (GetPlayerPositions(board, 10))
    #
    # tree_next = []
    #
    # for i in white_pos:
    #     tree_next += [GetPieceLegalMoves(board, i)]
    #
    # move_list = get_move_lists(white_pos, tree_next)
    #
    # board_next = []
    # a = next_board(board, move_list[0]) # move is of the form [position 1, position 2]
    #
    # for i in move_list:
    #     board_next += [next_board(board, i)]
    #
    # print("")
    # print("==============================================")
    #
    # board = get_new_board()
    # print("Board at 48: ", board[48])
    # board[48] = 10
    #
    # print_num_board(board)
    # print(board)
    #
    # print(eval_board(board))
    #
    # print("\n==============================================")

    node_a = BoardTreeNode(get_new_board(), 10)
    print(node_a.go_deeper())
    node_a.go_deeper()
    node_a.go_deeper()
    node_a.go_deeper()
    # node_a.go_deeper()
    print_num_board(node_a.children[8].children[8].children[8].children[8].board)

    node_a.rate_children()

    print(node_a.move_ratings)





main()
