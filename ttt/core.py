import collections

from util import count_each_item
from util import flatten
from util import memoize

Board  = collections.namedtuple("Board"  , "size moves")
Cell   = collections.namedtuple("Cell"   , "row_id col_id")
Player = collections.namedtuple("Player" , "name strategy")


def print_board(board):
  print board

  boardArray = []
  for i in range(board.size):
    boardArray.append(['-' for j in range(board.size)])

  mark = "X"
  for cell in board.moves:
    if mark == "X":
      mark = "0"
    else:
      mark = "X"

    boardArray[cell.row_id][cell.col_id] = mark

  for line in boardArray:
    print line

  print '--------'

def play_move(board, one, two):
  ret = validate_board(add_move_to_board(board, validate_move(board, one.strategy(board)), False,False),
                                                one.name, lambda board: play_move(board, two, one))
  #print_board(board)
  return ret

def _add_move_to_board(board, move,printBoard=False,printMove=False):
  ret = Board(board.size, board.moves + (move,))
  if printMove==True:
    print move

  if printBoard==True:
    print_board(ret)
  return ret

def _last_player_has_won(board):
  ret = any([all([cell in get_moves_of_last_player(board) for cell in line]) for line in get_lines(board)])
  return ret

def _play_double_games (size, ndouble_games, one, two):
  games = []
  for i in xrange(ndouble_games):
    print "Playing double game = " + str(i)
    games.append(play_double_game(size, one, two))
    print "Played double game = " + str(i)

  return flatten(games)

add_move_to_board        = _add_move_to_board
board_is_full            = lambda board       : len(get_free_cells(board)) == 0
create_empty_board       = lambda size        : Board(size, ())
get_cells                = lambda board       : [Cell(row_id, col_id) for row_id in range(board.size) for col_id in range(board.size)]
get_columns              = lambda board       : [[Cell(row_id, col_id) for row_id in range(board.size)] for col_id in range(board.size)]
get_diagonals            = lambda board       : [[Cell(n, n) for n in range(board.size)], [Cell(n, board.size-1-n) for n in range(board.size)]]
get_free_cells           = lambda board       : [cell for cell in get_cells(board) if cell not in board.moves]
get_lines                = lambda board       : get_rows(board) + get_columns(board) + get_diagonals(board)
get_moves_of_last_player = lambda board       : board.moves[1 - len(board.moves) % 2::2]
get_rows                 = lambda board       : [[Cell(row_id, col_id) for col_id in range(board.size)] for row_id in range(board.size)]
last_player_has_won      = _last_player_has_won


def validate_move(board, move):
  assert move in get_free_cells(board)
  return move

play_double_game  = lambda size, one, two                : [play_game(size, one, two), play_game(size, two, one)]
play_double_games = _play_double_games
play_game         = lambda size, one, two                : play_move(create_empty_board(size), one, two)
play_match        = lambda size, ndouble_games, one, two : count_each_item(play_double_games(size, ndouble_games, one, two))
validate_board    = lambda board, name, play_next_move   : (name if last_player_has_won(board) else "<DRAW>" if  board_is_full(board) else play_next_move(board))
