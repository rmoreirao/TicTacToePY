from ttt import core

def strategy(board):
  return core.get_free_cells(board)[0]
