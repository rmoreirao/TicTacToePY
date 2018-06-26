from strategies import simple
from ttt import core
import collections
import math
from ttt.util import memoize

TurnBrazucaScore = collections.namedtuple("TurnBrazucaScore", "name strategy")

class BrazucaScore:
    WIN_WEIGHT = 10.0
    DRAW_WEIGHT = 0
    LOSS_WEIGHT = -30.0
    ROUND_WEIGHT = -2.0

    def __init__(self,round, win, loss, draw):
        self.round = round
        self.draw = draw
        self.loss = loss
        self.win = win

    def add(self,result):
        if self.round != result.round:
            raise Exception("Round is different! You cannot sum it!")
        return BrazucaScore(result.round,self.win + result.win, self.loss + result.loss, self.draw + result.draw)

    def come_to_a_number(self):
        # Round is inversely weighted! First round has more weight!
        lossSum = (self.LOSS_WEIGHT * self.loss) * abs(math.pow(self.round, self.ROUND_WEIGHT))
        winSum = (self.WIN_WEIGHT * self.win) * abs(math.pow(self.round, self.ROUND_WEIGHT))
        drawSum = (self.draw * self.DRAW_WEIGHT) * abs(math.pow(self.round, self.ROUND_WEIGHT))
        finalNumber = drawSum + winSum + lossSum
        return finalNumber

    def only_loose(self):
        return self.win == 0.0 and self.draw == 0.0 and self.loss > 0.0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "round={0}, winCount={1}, lossCount={2},drawCount={3}, come_to_a_number={4}".format(self.round,self.win, self.loss, self.draw, self.come_to_a_number())

def create_zero(round):
    return BrazucaScore(round,0.0, 0.0, 0.0)

def create_draw(round):
    return BrazucaScore(round,0.0, 0.0, 1.0)

def create_win(round):
    return BrazucaScore(round,1.0, 0.0, 0.0)

def create_loss(round):
    return BrazucaScore(round,0.0, 1.0, 0.0)

def _calculateScoreRecurrent(board, currentCell,scoreSign,round):
    cellSimulationBoard = core.add_move_to_board(board,currentCell)
    #core.print_board(cellSimulationBoard)

    if core.last_player_has_won(cellSimulationBoard):
        if scoreSign >= 0:
            return [create_win(round)]
        return [create_loss(round)]
    elif core.board_is_full(cellSimulationBoard):
        return [create_draw(round)]
    else:
        totalScore = {}
        for freeCell in core.get_free_cells(cellSimulationBoard):
            scores = calculateScoreRecurrent(cellSimulationBoard, freeCell, scoreSign * -1, round + 1)

            for score in scores:
                scoreForRound = totalScore.setdefault(score.round, create_zero(score.round))
                totalScore[score.round] = score.add(scoreForRound)

        return totalScore.values()

calculateScoreRecurrent = memoize(_calculateScoreRecurrent)
#calculateScoreRecurrent = _calculateScoreRecurrent

def getNextBrazucaMove(board):
    simulationResult = {}
    for cell in core.get_free_cells(board):
        #print "Checking Cell " + str(cell)
        #core.print_board(board)
        scores = calculateScoreRecurrent(board, cell, 1, 1)
        if True in [x.only_loose() for x in scores if x.round <= 2]:
            # If the move leads to a situation where I only loose on the next round of the other player, then discard it!
            print "Discarding " + str(scores)
            continue

        finalScore = sum([x.come_to_a_number() for x in scores])
        print(str(scores) + "FinalScore=" + str(finalScore))
        simulationResult[cell] = finalScore

    if(len(simulationResult) == 0):
        print "No Strategy has been found! Going to SimpleStrategy!"
        return simple.strategy(board)

    maxScoreCell = max(simulationResult.iterkeys(), key=lambda x: simulationResult[x])

    #print "move: " + str(maxScoreCell) + " & score: " + str(simulationResult[maxScoreCell]) + " & simulationResult: " + str(simulationResult)
    return maxScoreCell


def strategy(board):
    move = getNextBrazucaMove(board)

    print "Brazuca Choice: " + str(move)
    return move
