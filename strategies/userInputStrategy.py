import random

from ttt import core

def strategy(board):
  row = raw_input("Row? ")
  column = raw_input("Column? ")
  return core.Cell( row_id=int(row)-1,col_id=int(column)-1)
