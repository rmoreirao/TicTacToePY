import random

from ttt import core
from ttt.util import memoize

MIN_SCORE = -1
MAX_SCORE = 1

def _calculateBrazucaTreeNodesRecurrent(board, cell, depth, max_depth):
    player = depth % 2
    cellSimulationBoard = core.add_move_to_board(board,cell)

    if core.last_player_has_won(cellSimulationBoard):
        if player == 0:
            return MAX_SCORE
        else:
            return MIN_SCORE
    elif core.board_is_full(cellSimulationBoard) or depth >= max_depth:
        return 0
    else:
        if player == 0:
            minScore = MAX_SCORE

            for freeCell in core.get_free_cells(cellSimulationBoard):
                score = calculateBrazucaTreeNodesRecurrent(cellSimulationBoard, freeCell, depth + 1, max_depth)
                if score <= MIN_SCORE:
                    return score
                minScore = min(minScore, score)
            return minScore

        else:
            highestScore = MIN_SCORE
            for freeCell in core.get_free_cells(cellSimulationBoard):
                score = calculateBrazucaTreeNodesRecurrent(cellSimulationBoard, freeCell, depth + 1, max_depth)
                if score >= MAX_SCORE:
                    return score

                highestScore = max(highestScore, score)
            return highestScore

# calculateBrazucaTreeNodesRecurrent = memoize(_calculateBrazucaTreeNodesRecurrent)
calculateBrazucaTreeNodesRecurrent = _calculateBrazucaTreeNodesRecurrent

def _getNextBrazucaMove(board):
    free_cells = core.get_free_cells(board)

    max_depth = get_max_depth(board, free_cells)

    simulationResult = {}
    for i in random.sample(range(len(free_cells)), len(free_cells)):
        cell = free_cells[i]
        score = calculateBrazucaTreeNodesRecurrent(board, cell, 0 , max_depth)
        # if score >= MAX_SCORE:
        #     return cell
        simulationResult[cell] = score

    maxScoreCell = max(simulationResult.iterkeys(), key=lambda x: simulationResult[x])

    return maxScoreCell


def get_max_depth(board, free_cells):
    if (board.size == 3):
        max_depth = 8
    else:
        if len(free_cells) > 8:
            max_depth = 3
        else:
            max_depth = 4
    return max_depth


getNextBrazucaMove = memoize(_getNextBrazucaMove)

def strategy(board):
    bestMove = getNextBrazucaMove(board)
    return bestMove
