from tile import Tile
from board import Board
from piece import *

chessBoard = Board()
chessBoard.makeBoard()
chessBoard.populate()
print(chessBoard.board[Tile.coordinateToMailbox('B2')].piece.mailbox)

chessBoard.board[Tile.coordinateToMailbox('B2')].piece.generateMoves(chessBoard.board)
print("legal moves: " , chessBoard.board[Tile.coordinateToMailbox('B2')].piece.legalMoves, end='\n\n')
chessBoard.display()
chessBoard.addPiece('Q','white','D4')
chessBoard.addPiece('P','white','b4')
chessBoard.addPiece('P','black','c3')
chessBoard.addPiece('R','black','c4')
chessBoard.addPiece('B','black','e5')
chessBoard.display()
chessBoard.board[Tile.coordinateToMailbox('B2')].piece.generateMoves(chessBoard.board)
print("legal moves for B2 white Pawn: " , chessBoard.board[Tile.coordinateToMailbox('B2')].piece.legalMoves, end='\n\n')
chessBoard.board[Tile.coordinateToMailbox('B1')].piece.generateMoves(chessBoard.board)
print("legal moves for B1 white Knight: " , chessBoard.board[Tile.coordinateToMailbox('B1')].piece.legalMoves, end='\n\n')
chessBoard.board[Tile.coordinateToMailbox('E1')].piece.generateMoves(chessBoard.board)
print("legal moves for E1 white King: " , chessBoard.board[Tile.coordinateToMailbox('E1')].piece.legalMoves, end='\n\n')
chessBoard.board[Tile.coordinateToMailbox('D4')].piece.generateMoves(chessBoard.board)
print("legal moves for D4 white Queen: " , chessBoard.board[Tile.coordinateToMailbox('D4')].piece.legalMoves, end='\n\n')
chessBoard.board[Tile.coordinateToMailbox('c4')].piece.generateMoves(chessBoard.board)
print("legal moves for C4 black Rook: " , chessBoard.board[Tile.coordinateToMailbox('c4')].piece.legalMoves, end='\n\n')
chessBoard.board[Tile.coordinateToMailbox('e5')].piece.generateMoves(chessBoard.board)
print("legal moves for E5 black Bishop: " , chessBoard.board[Tile.coordinateToMailbox('e5')].piece.legalMoves, end='\n\n')
chessBoard.generatePieceList()
chessBoard.generateMoves()

input() 
