# Core Functionality Functions from B2

def GetPlayerPositions(board, player):
	retVal = []
	for i in range(len(board)):
		if(player_at_position(i, board) == player):
			retVal += [i]

	return retVal

# TODO: Make this into a set of functions instead of if statements.
def GetPieceLegalMoves(board, position): # position is the index of the piece on the board list (1-D)
	piece_num = board[position] # piece_num is the ID of the piece (10 = white pawn, 21 = black knight, etc.)
	ret_list = [] # value we will return that contains the list of next moves for that piece

	if(piece_num == 0): # if the ID is 0, it is an empty space, so we return an empty list
		print("INVALID: You can't move an empty space!")
		return ret_list

	coords = coord_from_num(position) #These are the 0-indexed positions of each piece. top left is 0,0.
	row = coords[0]
	col = coords[1]

	player = (piece_num // 10) * 10
	oppo = -1
	if(player == 10):
		oppo = 20
	elif(player == 20):
		oppo = 10
	else:
		print("INVALID: Player is not 10 or 20.")

	# Case for Pawn: Preliminary tests positive
	if(piece_num % 10 == 0):
		if piece_num == 10: # White, going down
			if(player_at_position(num_from_coord([row+1, col]), board) == 0):
				ret_list += [num_from_coord([row+1, col])]
			if(player_at_position(num_from_coord([row+1, col+1]), board) == 20):
				ret_list += [num_from_coord([row+1, col+1])]
			if(player_at_position(num_from_coord([row+1, col-1]), board) == 20):
				ret_list += [num_from_coord([row+1, col-1])]

		elif piece_num == 20:
			if(player_at_position(num_from_coord([row-1, col]), board) == 0):
				ret_list += [num_from_coord([row-1, col])]
			if(player_at_position(num_from_coord([row-1, col+1]), board) == 10):
				ret_list += [num_from_coord([row-1, col+1])]
			if(player_at_position(num_from_coord([row-1, col-1]), board) == 10):
				ret_list += [num_from_coord([row-1, col-1])]

		return ret_list

	# Case for Knight: Preliminary tests are positive.
	if(piece_num % 10 == 1):
		knight_nums = []
		knight_nums += [num_from_coord([row+2, col+1])]
		knight_nums += [num_from_coord([row+2, col-1])]
		knight_nums += [num_from_coord([row-2, col+1])]
		knight_nums += [num_from_coord([row-2, col-1])]

		knight_nums += [num_from_coord([row+1, col+2])]
		knight_nums += [num_from_coord([row-1, col+2])]
		knight_nums += [num_from_coord([row+1, col-2])]
		knight_nums += [num_from_coord([row-1, col-2])]

		# Check the following:
			# if entry is -1, pick it out
			# if player at that num is the player, pick it out.
			# yup.

		i = 0
		while i < len(knight_nums):
			if(knight_nums[i] == -1):
				knight_nums.pop(i)
				i -= 1
			if(player_at_position(knight_nums[i], board) == player):
				knight_nums.pop(i)
				i -= 1
			# print(knight_nums)
			i += 1


		return knight_nums

	# Rook case: Passed preliminary tests
	if piece_num % 10 == 3:
		# Part 1: Checking to the right
		rook_nums = []
		for i in range(col+1, 8, 1):
			rook_nums += [num_from_coord([row, i])]
			if board[num_from_coord([row, i])] != 0:
				break

		for i in range(col-1, -1, -1):
			rook_nums += [num_from_coord([row, i])]
			if board[num_from_coord([row, i])] != 0:
				break

		for i in range(row+1, 8, 1):
			rook_nums += [num_from_coord([i, col])]
			if board[ num_from_coord([i, col]) ] != 0:
				break

		for i in range(row-1, -1, -1):
			rook_nums += [num_from_coord([i, col])]
			if board[ num_from_coord([i, col]) ] != 0:
				break

		# Now checking if we're killing one of our own pieces
		# i = 0
		# while(i < len(rook_nums)):
		# 	if player_at_position(rook_nums[i], board) == player:
		# 		rook_nums.pop(i)
		# 		i -= 1
		# 	i += 1

		rook_nums = filter_moves(rook_nums, board, player)

		return rook_nums

	# Passed initial Tests
	if piece_num % 10 == 2: # Bishop case
		# Part 1: Checking to the right
		bish_nums = []

		for i in range(1,8,1):
			bish_nums += [num_from_coord([row+i, col+i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row-i, col+i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row+i, col-i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row-i, col-i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break



		# Now checking if we're killing one of our own pieces or are out of bounds
		# i = 0
		# while(i < len(bish_nums)):
		# 	if player_at_position(bish_nums[i], board) == player:
		# 		bish_nums.pop(i)
		# 		i -= 1
		# 	i += 1
		bish_nums = filter_moves(bish_nums, board, player)

		return bish_nums

	if piece_num % 10 == 4: # Queen case
		# Part 1: Getting Bishop Case
		bish_nums = []

		for i in range(1,8,1):
			bish_nums += [num_from_coord([row+i, col+i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row-i, col+i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row+i, col-i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break

		for i in range(1, 8, 1):
			bish_nums += [num_from_coord([row-i, col-i])]
			if board[bish_nums[len(bish_nums)-1]] != 0:
				break



		# Now checking if we're killing one of our own pieces or are out of bounds
		# i = 0
		# while(i < len(bish_nums)):
		# 	if player_at_position(bish_nums[i], board) == player:
		# 		bish_nums.pop(i)
		# 		i -= 1
		# 	i += 1

		# Part 1: Checking to the right
		rook_nums = []
		for i in range(col+1, 8, 1):
			rook_nums += [num_from_coord([row, i])]
			if board[num_from_coord([row, i])] != 0:
				break

		for i in range(col-1, -1, -1):
			rook_nums += [num_from_coord([row, i])]
			if board[num_from_coord([row, i])] != 0:
				break

		for i in range(row+1, 8, 1):
			rook_nums += [num_from_coord([i, col])]
			if board[ num_from_coord([i, col]) ] != 0:
				break

		for i in range(row-1, -1, -1):
			rook_nums += [num_from_coord([i, col])]
			if board[ num_from_coord([i, col]) ] != 0:
				break

		# Now checking if we're killing one of our own pieces
		# i = 0
		# while(i < len(rook_nums)):
		# 	if player_at_position(rook_nums[i], board) == player:
		# 		rook_nums.pop(i)
		# 		i -= 1
		# 	i += 1

		queen_nums = rook_nums + bish_nums

		queen_nums = filter_moves(queen_nums, board, player)

		return queen_nums + queen_nums

	if piece_num % 10 == 5: # King's case
		king_nums = []

		# Part 1: Getting Bishop Case
		bish_nums = []

		for i in range(1,8,1):
			bish_nums += [num_from_coord([row+i, col+i])]
			bish_nums += [num_from_coord([row-i, col+i])]
			bish_nums += [num_from_coord([row+i, col-i])]
			bish_nums += [num_from_coord([row-i, col-i])]

			bish_nums += [num_from_coord([row+i, col])]
			bish_nums += [num_from_coord([row-i, col])]
			bish_nums += [num_from_coord([row, col-i])]
			bish_nums += [num_from_coord([row, col+i])]
			break

		# Now checking if we're killing one of our own pieces
		# i = 0
		# while(i < len(bish_nums)):
		# 	if player_at_position(bish_nums[i], board) == player or player_at_position(bish_nums[i], board) == -1:
		# 		bish_nums.pop(i)
		# 		i -= 1
		# 	i += 1

		bish_nums = filter_moves(bish_nums, board, player)

		return bish_nums

	print("Invalid: The number",position," is not a valid piece/space identifier")

def IsPositionUnderThreat(board, position, player):
	return

# Helper Functions for Debugging Here

def get_move_lists(cur_positions, nexts):
	retVal = []

	for i in range(len(cur_positions)):
		for j in nexts[i]:
			cur_position = cur_positions[i]
			alternative = j
			tmp = [cur_position, alternative]
			retVal += [tmp]

	return retVal

def next_board(board, move):
	board2 = []

	for i in board:
		board2 += [i];

	board2[move[1]] = board2[move[0]]
	board2[move[0]] = 0

	return board2

def filter_moves(moves, board, player):
	move2 = []
	i = 0
	while(i < len(moves)):
		if not (player_at_position(moves[i], board) == player or player_at_position(moves[i], board) == -1):
			move2 += [moves[i]]
		i += 1


	return move2

def player_at_position(num, board): #10 if white, 20 if black, 0 if nothing, -1 if out of bounds
	if(num < 0 or num >= len(board)):
		return -1
	piece_num = board[num]
	if(piece_num == 0):
		return 0
	else:
		return (piece_num//10)*10

def reset_type():
	print("\033[1;37;40m", end="")

def coord_from_num(num):
	row = num//8
	col = num%8
	return[row, col]

def num_from_coord(coord):
	if coord[0] >= 8 or coord[1] >= 8:
		return -1
	elif(coord[0] < 0 or coord[1] < 0):
		return -1
	return coord[0]*8 + coord[1]

def get_human_move(player, board): #10 = white, 20 = black. Returns a new board.
	board2 = board #TODO: Make/implement deepcopy function

	piece_num = -1

	while(piece_num == -1):
		str_in = input("\033[1;37;40mPiece Coordinates: ")
		space_ind = str_in.index(" ")
		if(space_ind == -1):
			print("INVALID: No space in input")
			piece_num = -1
		row = int(str_in[0:space_ind])
		col = int(str_in[space_ind:])

		# row -= 1;
		# col -= 1;
		coord = [row, col]
		piece_num = num_from_coord(coord)
		if(board2[piece_num] == 0):
			print("INVALID: You can't move an empty space!")
			piece_num = -1;
		elif( (board2[piece_num])//10 * 10 != player):
			print("INVALID: You can't move your opponent's piece!")
			piece_num = -1;
		elif(piece_num < 0):
			print("INVALID: You can't move a negative space!")
			piece_num = -1

	destination_num = -1

	while(destination_num == -1):
		str_in = input("\033[1;37;40mDestination Coordinates: ")
		space_ind = str_in.index(" ")
		if(space_ind == -1):
			print("INVALID: No space in input")
			piece_num = -1
		row = int(str_in[0:space_ind])
		col = int(str_in[space_ind:])

		# row -= 1;
		# col -= 1;
		coord = [row, col]
		destination_num = num_from_coord(coord)
		GetPieceLegalMoves(board2, destination_num)
		if(False and destination_num not in GetPieceLegalMoves(board2, destination_num)):#TODO: Implement GetPieceLegalMoves function
			print("INVALID: That was an invalid move for that piece!")
			piece_num = -1;
		elif((board2[destination_num]//10) * 10 == player):
			print("INVALID: You can't capture your own piece!")
			piece_num = -1;


	board2[destination_num] = board2[piece_num]
	board2[piece_num] = 0

	return board2






def get_new_board():
	board = []
	for i in range(64):
		board += [0]

	for i in range(8,16,1):
		board[i] = 10

	for i in range(48,56,1):
		board[i] = 20

	board[0] = 13
	board[1] = 11
	board[2] = 12
	board[3] = 15
	board[4] = 14
	board[5] = 12
	board[6] = 11
	board[7] = 13

	board[56+0] = 23
	board[56+1] = 21
	board[56+2] = 22
	board[56+3] = 25
	board[56+4] = 24
	board[56+5] = 22
	board[56+6] = 21
	board[56+7] = 23

	return board

def print_num_board(board):
	strOut = ""

	print("========================")

	color_dict = {
		"green" : "32",
		"red" : "31",
		"cyan" : "36",
		"white" : "37",
		"blue" : "34"
	}

	cnt = 0
	for i in board:
		color = "blue"

		printChar = i;
		printChar = i%10;

		if printChar == 0:
			printChar = 'p'
		elif printChar == 1:
			printChar = 'n'
		elif printChar == 2:
			printChar = 'b'
		elif printChar == 3:
			printChar = 'r'
		elif printChar == 4:
			printChar = 'q'
		elif printChar == 5:
			printChar = 'K'

		if i == 0:
			if (cnt // 8 + cnt) % 2 == 0:
				printChar = "_"
			else:
				printChar = "#"

			printChar = str(cnt)
			if(cnt < 10):
				printChar += " "

		if i // 10  == 1:
			color = "cyan"
		if i // 10 == 2:
			color = "red"

		if(i != 0):
			print("\033[1;"+color_dict[color]+";40m", printChar, end=" ")
		else:
			print("\033[1;"+color_dict[color]+";40m", printChar, end="")
		cnt += 1;
		if(cnt % 8 == 0):
			print("")

	print("========================")
