class BoardModel(object):
	# static
	_board = {}
	
	def get_board(self):
        return type(self)._board

    def set_board(self,data):
        type(self)._board = data

    board = property(get_board, set_board)