from chessPlayer_trees import *
import time
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

    # node_a = BoardTreeNode(get_new_board(), 10)
    # node_a.go_deeper()
    # print(node_a.get_best_move())
    # node_a.go_deeper()
    # print(node_a.get_best_move())
    # node_a.go_deeper()
    # print(node_a.get_best_move())
    # node_a.go_deeper()
    # print(node_a.get_best_move())
    # node_a.go_deeper()
    # print_num_board(node_a.children[8].children[8].children[8].children[8].board)
    #
    # node_a.rate_children()
    #
    # print(node_a.move_ratings)


    board = get_new_board()
    me = 20
    computer = 10

    num_layers_down = 4

    while True:
        print_num_board(board)
        board = get_human_move(me, board)
        print_num_board(board)


        comp_ret = chessPlayer(board, computer)
        comp_move = comp_ret[1]


        board[comp_move[1]] = board[comp_move[0]]
        board[comp_move[0]] = 0
        # print(comp_ret[3])
        print_num_board(board)
        # root_node = BoardTreeNode(board, computer)
        #
        # for i in range(num_layers_down):
        #     root_node.go_deeper()
        #
        # comp_move = root_node.get_best_move()
        # board[comp_move[1]] = board[comp_move[0]]
        # board[comp_move[0]] = 0
        # print(chessPlayer(board, 10)[3])

    node_a = BoardTreeNode(get_new_board(), 10)
    node_a.generate_children()
    node_a.get_best_move()

    board = get_new_board()

    # board[]

    print(chessPlayer(board, 10)[3])





main()
