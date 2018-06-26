from strategies import simple
from ttt import core
import collections
import math
from ttt.util import memoize


class BrazucaTreeNode:
    def __init__(self, parent, cell, treeLevel ):
        self.parent = parent
        self.cell = cell
        self.treeLevel = treeLevel
        self.childs = []

    def append_child(self,childNode):
        self.childs.append(childNode)
        return self

    def set_content(self,player, board, result):
        # -1 = loss, 0=draw and 1 = win
        self.result = result
        self.board = board
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "cell={0}, treeLevel={1}, result={2}".format(self.cell,self.treeLevel,self.result)


def calculate_tree_node_winning_score(node):
        if len(node.childs) == 0:
            score = 0
            if float(node.result) >=0:
                score = node.result * 1.0
            else:
                score = node.result * 1.0
            node.score = score
            core.print_board(node.board)
            print "Score Leaf = " + str(score)
            return score
        else:
            childsScore = 0.0
            for child in node.childs:
                childsScore = childsScore + calculate_tree_node_winning_score(child)

            node.score = childsScore
            core.print_board(node.board)
            print "Score Node = " + str(childsScore)
            return childsScore / len(node.childs)

def calculateBrazucaTreeNodesRecurrent(board, currentNode):
    player = currentNode.treeLevel % 2
    cellSimulationBoard = core.add_move_to_board(board,currentNode.cell)

    if core.last_player_has_won(cellSimulationBoard):
        if player == 0:
            currentNode.set_content(player=player, board=cellSimulationBoard,result=1)
        else:
            currentNode.set_content(player=player, board=cellSimulationBoard, result=-1)
    elif core.board_is_full(cellSimulationBoard):
        currentNode.set_content(player=player, board=cellSimulationBoard,result=0)
    else:
        if player == 0:
            minScore = 1

            for freeCell in core.get_free_cells(cellSimulationBoard):
                newCurrentNode = BrazucaTreeNode(parent = currentNode, cell = freeCell, treeLevel = currentNode.treeLevel + 1)
                newCurrentNode.board = cellSimulationBoard
                currentNode.append_child(newCurrentNode)
                calculateBrazucaTreeNodesRecurrent(cellSimulationBoard,newCurrentNode)
                minScore = min(minScore, newCurrentNode.result)

            currentNode.result = minScore


        else:
            highestScore = -1
            for freeCell in core.get_free_cells(cellSimulationBoard):
                newCurrentNode = BrazucaTreeNode(parent=currentNode, cell=freeCell, treeLevel=currentNode.treeLevel + 1)
                newCurrentNode.board = cellSimulationBoard
                currentNode.append_child(newCurrentNode)
                calculateBrazucaTreeNodesRecurrent(cellSimulationBoard, newCurrentNode)
                highestScore = max(highestScore, newCurrentNode.result)

            currentNode.result = highestScore

# calculateBrazucaTreeNodesRecurrent = memoize(_calculateBrazucaTreeNodesRecurrent)

def getNextBrazucaMove(board):
    simulationResult = {}
    for cell in core.get_free_cells(board):
        #print "Checking Cell " + str(cell)
        #core.print_board(board)
        node = BrazucaTreeNode(parent=None,cell= cell,treeLevel=0)
        node.board = board

        calculateBrazucaTreeNodesRecurrent(board, node)
        #print("FinalScore=" + str(node.result))
        simulationResult[cell] = node.result

    maxScoreCell = max(simulationResult.iterkeys(), key=lambda x: simulationResult[x])
    # print "move: " + str(maxScoreCell) + " & score: " + str(simulationResult[maxScoreCell]) + " & simulationResult: " + str(simulationResult)
    return maxScoreCell

    return simple.strategy(board)


def strategy(board):
    bestMove = getNextBrazucaMove(board)

    print "Brazuca Choice: " + str(bestMove)
    return bestMove
