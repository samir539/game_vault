chess_pieces = {
    "White_King": "\u2654",
    "White_Queen": "\u2655",
    "White_Rook": "\u2656",
    "White_Bishop": "\u2657",
    "White_Knight": "\u2658",
    "White_Pawn": "\u2659",
    "Black_King": "\u265A",
    "Black_Queen": "\u265B",
    "Black_Rook": "\u265C",
    "Black_Bishop": "\u265D",
    "Black_Knight": "\u265E",
    "Black_Pawn": "\u265F"
}


class Game:
    def __init__(self,board,peices):
        self._board = board
        self._peices = peices
        
    def run_game(self):
        pass
        #game loop
        #rendering
        
    
    


if __name__ == "__main__":
    a,b = 5
    myGame = Game(a,b)
    myGame.run_game()