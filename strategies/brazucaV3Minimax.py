from strategies import simple
from ttt import core
import collections
import math
from ttt.util import memoize

def _calculateBrazucaTreeNodesRecurrent(board, cell, depth):
    player = depth % 2
    cellSimulationBoard = core.add_move_to_board(board,cell)

    if core.last_player_has_won(cellSimulationBoard):
        if player == 0:
            return 1
        else:
            return -1
    elif core.board_is_full(cellSimulationBoard):
        return 0
    else:
        if player == 0:
            minScore = 1

            for freeCell in core.get_free_cells(cellSimulationBoard):
                score = calculateBrazucaTreeNodesRecurrent(cellSimulationBoard, freeCell, depth + 1)
                minScore = min(minScore, score)
            return minScore

        else:
            highestScore = -1
            for freeCell in core.get_free_cells(cellSimulationBoard):
                score = calculateBrazucaTreeNodesRecurrent(cellSimulationBoard, freeCell, depth + 1)
                highestScore = max(highestScore, score)

            return highestScore

calculateBrazucaTreeNodesRecurrent = memoize(_calculateBrazucaTreeNodesRecurrent)

def getNextBrazucaMove(board):
    simulationResult = {}
    for cell in core.get_free_cells(board):
        score = calculateBrazucaTreeNodesRecurrent(board, cell, 0)
        simulationResult[cell] = score

    maxScoreCell = max(simulationResult.iterkeys(), key=lambda x: simulationResult[x])
    return maxScoreCell


def strategy(board):
    bestMove = getNextBrazucaMove(board)

    # print "Brazuca Choice: " + str(bestMove)
    return bestMove
