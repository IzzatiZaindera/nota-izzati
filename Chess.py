class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        
    def move(self, new_position):
        self.position = new_position
        
class King(Piece):
    def is_valid_move(self, new_position):
        return abs(new_position[0] - self.position[0]) <= 1 and abs(new_position[1] - self.position[1]) <= 1
        
class Queen(Piece):
    def is_valid_move(self, new_position):
        return (new_position[0] == self.position[0] or new_position[1] == self.position[1] or
                abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]))
    
class Rook(Piece):
    def is_valid_move(self, new_position):
        return (new_position[0] == self.position[0] or new_position[1] == self.position[1] or
                abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]))
    
class Knight(Piece):
    def is_valid_move(self, new_position):
        return (new_position[0] == self.position[0] or new_position[1] == self.position[1] or
                abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]))
    
class Bishop(Piece):
    def is_valid_move(self, new_position):
        return (new_position[0] == self.position[0] or new_position[1] == self.position[1] or
                abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]))
    
class Pawn(Piece):
    def is_valid_move(self, new_position):
        return (new_position[0] == self.position[0] or new_position[1] == self.position[1] or
                abs(new_position[0] - self.position[0]) == abs(new_position[1] - self.position[1]))





# Initialize chess board with starting positions of pieces
board = [[Rook("black", (0, 0)), Knight("black", (0, 1)), Bishop("black", (0, 2)),
          Queen("black", (0, 3)), King("black", (0, 4)), Bishop("black", (0, 5)),
          Knight("black", (0, 6)), Rook("black", (0, 7))],
         [Pawn("black", (1, i)) for i in range(8)],
         [None for i in range(8)] * 6,
         [Pawn("white", (6, i)) for i in range(8)],
         [Rook("white", (7, 0)), Knight("white", (7, 1)), Bishop("white", (7, 2)),
          Queen("white", (7, 3)), King("white", (7, 4)), Bishop("white", (7, 5)),
          Knight("white", (7, 6)), Rook("white", (7, 7))]]

# Example move
piece = board[1][1]
new_position = (2, 2)
if piece.is_valid_move(new_position):
    piece.move(new_position)
else:
    print("Invalid move")