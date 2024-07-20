from pieces import AbstractChessPiece,Pawn,Rook,Knight,Bishop,Queen,King
from board import Board
from game_functions import make_pieces
from support_functions import format_of_move_valid, move_convert, format_of_move_valid_alpha_numeric


class Game:
    def __init__(self,board):
        self._board = board
        self._running = True
        self._player_turn = 1
        
    @property
    def board(self):
        return self._board
    
    @property
    def player_turn(self):
        return self._player_turn
    
        
    def run_game(self):
        self._board.render()
        while self._running:
            if self.board.look_for_check(self.player_turn): #investigate check
                if self.board.look_for_checkmate(self.player_turn): #investigate checkmate
                    print(f"It is checkmate and player {self.player_turn} has lost")
                    self._running = False
                    break
                
                #prompt user to escape check
                while True:
                    move = input(f"It is check for player {self.player_turn}, please address this...")
                    while not format_of_move_valid_alpha_numeric(move):
                        move = input(f"It is check for player {self.player_turn}, please address this...")
                    move = move_convert(move)
                    _, friendly, enemy = self.board.update_board(move, self.player_turn, simulated_update=True)
                    if not self.board.look_for_check(self.player_turn, friendly, enemy):
                        self.board.update_board(move, self.player_turn, simulated_update=False)
                        break
            else:
                move = input(f"{self.player_turn} please make a move\n")
                while not format_of_move_valid_alpha_numeric(move):
                    move = input(f"{self.player_turn} please make a move\n")
                move = move_convert(move)
                print(self.board.update_board(move,self.player_turn))        
            self._board.render()
            self._player_turn ^= 1
        #game loop
        #rendering


if __name__ == "__main__":
    #generate starting pieces
    white_pieces, black_pieces = make_pieces()
    game_board = Board(white_pieces, black_pieces)
    myGame = Game(game_board)
    myGame.run_game()
    # a,b = 5
    # myGame = Game(a,b)
    # myGame.run_game()