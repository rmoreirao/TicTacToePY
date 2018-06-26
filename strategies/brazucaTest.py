# Special Thanks To:
# https://github.com/omegadeep10/tic-tac-toe/blob/master/game.py
# https://en.wikipedia.org/wiki/Minimax

import ttt.core as core
import inspect

from strategies import brazuca, brazucaV1

testStrategy = brazuca.strategy

def cellEquals(actualCell,expectedCell):
        pass

def validateCellsOR(scenarioName,actualCell,expectedCells):
    noFailure = False
    for cell in expectedCells:
        try:
            validateCell(scenarioName,actualCell,cell)
            noFailure = True
        except:
            pass

    if noFailure == False:
        raise Exception(scenarioName + " NOK!")

def validateCell(scenarioName,actualCell,expectedCell):
    if actualCell.row_id == expectedCell.row_id and expectedCell.col_id == actualCell.col_id:
        print scenarioName + " OK!"
    else:
        raise Exception(scenarioName + " NOK!" + " Expected: " + str(expectedCell) + " Actual: " + str(actualCell))

# X-0
# X-0
# ---
#Expected: Row = 2 and Col = 0 OR Row = 2 and Col = 2
def validateScenario1():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board,core.Cell(0,0))
    board = core.add_move_to_board(board, core.Cell(0, 2))
    board = core.add_move_to_board(board, core.Cell(1, 0))
    board = core.add_move_to_board(board, core.Cell(1, 2))
    ret = testStrategy(board)
    validateCellsOR(inspect.stack()[0][3], ret, [core.Cell(row_id=2,col_id=0), core.Cell(row_id=2,col_id=2)])

# 00-
# XX0
# X0-
#Expected: Row = 0 and Col = 2
def validateScenario2():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board,core.Cell(0,0))
    board = core.add_move_to_board(board, core.Cell(0, 1))
    board = core.add_move_to_board(board, core.Cell(1, 0))
    board = core.add_move_to_board(board, core.Cell(1, 1))
    board = core.add_move_to_board(board, core.Cell(1, 2))
    board = core.add_move_to_board(board, core.Cell(2, 0))
    board = core.add_move_to_board(board, core.Cell(2, 1))
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=0,col_id=2))

# 0--
# ---
# ---
#Expected: Row = 1 & Col = 1
def validateScenario3():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board,core.Cell(0,0))
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(1,1))

# -X-
# 0X-
# 0-0
#Expected: Row = 2 & Col = 0
def validateScenario4():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(1, 0))
    board = core.add_move_to_board(board, core.Cell(1, 1))
    board = core.add_move_to_board(board, core.Cell(2, 2))
    board = core.add_move_to_board(board, core.Cell(0, 1))
    board = core.add_move_to_board(board, core.Cell(2, 0))
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=2,col_id=1))

# ---
# -0-
# ---
#Expected: Row = 2 & Col = 1
def validateScenario5():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(1, 1))
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(col_id=0,row_id=0))

# X--
# 00-
# ---
#Expected: Row = 1 & Col = 2
def validateScenario6():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=1))
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=0))
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=0))
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=1,col_id=2))

# 0-X
# -X-
# --0
#Expected: Row = 1 & Col = 2
def validateScenario7():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=0))
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=1))
    board = core.add_move_to_board(board, core.Cell(row_id=2, col_id=2))
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=2))
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=2,col_id=0))

# 0-X
# XX-
# 0-0
#Expected: Row = 1 & Col = 2
def validateScenario8():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=0))
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=1))
    board = core.add_move_to_board(board, core.Cell(row_id=2, col_id=2))
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=2))
    board = core.add_move_to_board(board, core.Cell(row_id=2, col_id=0))
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=0))
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=2,col_id=1))


def validateScenario9():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(row_id=0, col_id=0))
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=1))
    board = core.add_move_to_board(board, core.Cell(row_id=2, col_id=2))
    # 0--
    # -X-
    # --0
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=0,col_id=1))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -X-
    # --0
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=2, col_id=1))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -X-
    # -00
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=2, col_id=0))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -X-
    # X00
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=0, col_id=2))
    board = core.add_move_to_board(board, ret)

    # 0X0
    # -X-
    # X00
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=1, col_id=2))
    board = core.add_move_to_board(board, ret)

    # 0X0
    # -XX
    # X00
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=1, col_id=0))

def validateScenario10():
    board = core.create_empty_board(3)
    board = core.add_move_to_board(board, core.Cell(row_id=1, col_id=1))
    # ---
    # -X-
    # ---
    # Expected: Row = 0 & Col = 1
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3],ret, core.Cell(row_id=0,col_id=0))
    board = core.add_move_to_board(board, ret)

    # 0--
    # -X-
    # ---
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=0, col_id=1))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -X-
    # ---
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=2, col_id=1))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -X-
    # -0-
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=1, col_id=2))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # -XX
    # -0-
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=1, col_id=0))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # 0XX
    # -0-
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=2, col_id=0))
    board = core.add_move_to_board(board, ret)

    # 0X-
    # 0XX
    # X0-
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=0, col_id=2))
    board = core.add_move_to_board(board, ret)

    # 0X0
    # 0XX
    # X0-
    core.print_board(board)
    ret = testStrategy(board)
    validateCell(inspect.stack()[0][3], ret, core.Cell(row_id=2, col_id=2))

validateScenario1();
validateScenario2();
validateScenario3();
validateScenario4();
#validateScenario5();
validateScenario6();
validateScenario7();
validateScenario8();
# validateScenario9();
# validateScenario10();