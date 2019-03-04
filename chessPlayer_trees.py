from chessPlayer_B2 import *

'''
my_board is a 64-long array
children_list is a list of BoardTreeNode's.
'''
class BoardTreeNode:
    # def __init__(self, my_board, children_list):
    #     print("DONT USE THIS INITIALIZER")
    #     self.board = my_board
    #     self.children = children_list
    #     self.moves = []
    #     self.move_ratings = []
    #     self.cur_player = 0

    def __init__(self, my_board, player):
        self.board = my_board
        self.children = []
        self.moves = []
        self.move_ratings = []
        self.cur_player = player
        opp = player+10
        if opp == 30:
            opp = 10
        self.cur_oppo = opp

    def add_child(self, child_board):
        self.children += child_board

    # This function adds another layer onto the tree
    def go_deeper(self):
        if not self.children:
            self.generate_children()
            return True

        for i in range(len(self.children)):
            (self.children[i]).go_deeper()


    # Adds children based on self's board and a player value
    def generate_children(self): # player is the player currently making
        # the move (we're generating a set of moves for them)
        if self.children:
            print("INVALID: Can't generate children when we already have children")
            return False

        player_pos = GetPlayerPositions(self.board, self.cur_player)

        children_next = []

        for i in player_pos:
            children_next += [GetPieceLegalMoves(self.board, i)]

        move_list = get_move_lists(player_pos, children_next)

        self.moves = move_list

        board_next = []

        for i in move_list:
            board_next += [next_board(self.board, i)]

        BTN_next = []

        for i in board_next:
            BTN_next += [BoardTreeNode(i, self.cur_oppo)]

        self.children = BTN_next

        return True;

    # This will populate the move_ratings for this particular node
    # It will be as long as the number of potential moves and will have a float for each of those moves.
    def rate_children(self): # returns a rating for this given node
        if not self.children: # we have no children
            print("INVALID: Cannot evaluate children of node with no children")
            return False
            # return eval_board(self.board)
        children_rating_list = []

        for i in self.children:
            deepest_ratings = i.get_rating_list_deepests()
            # print(deepest_ratings)
            children_rating_list += [float(sum(deepest_ratings))/float(len(deepest_ratings))]

        self.move_ratings = children_rating_list

    # This will try to get a float rating for the deepest children of this node.
    # We are going to go as deep as possible
    def get_rating_list_deepests(self):
        if not self.children:
            return [eval_board(self.board)]

        ret_list = []

        for i in self.children:
            ret_list += i.get_rating_list_deepests()

        return ret_list
