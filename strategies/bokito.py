import random

from ttt import core

def strategy(board):
  ret = random.choice(core.get_free_cells(board))
  # print "Bokito Choice: " + str(ret)
  return ret
