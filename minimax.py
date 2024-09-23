from TreeDatatype import Node # import modified Binary tree data structure, function only compatible with this
from math import inf

def Minimax(root: Node, Maximising: bool, depth=0, alpha=-inf, beta=inf):
    minDepth = inf
    if len(root.children) == 0:
        return (root.data, root.board)
    if Maximising: # Maximise
        bestVal = -inf
        bestboard = []
        for i in root.children:
            if i.data == None:
                value, _, depthv = Minimax(i, not(Maximising), depth+1, alpha, beta)
            else:
                value = i.data
                depthv = depth+1
            if bestVal < value:
                    bestVal = value
                    bestboard = i.board
            elif bestVal == value:
                if minDepth > depthv:
                    minDepth = depthv
                    bestboard = i.board
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
    else: # Minimise
        bestVal = inf
        bestboard = []
        for i in root.children:
            if i.data == None:
                value, _, depthv = Minimax(i, not(Maximising), depth+1, alpha, beta)
            else:
                value = i.data
                depthv = depth+1
            if bestVal > value:
                bestVal = value
                bestboard = i.board
            elif bestVal == value:
                if minDepth > depthv:
                    minDepth = depthv
                    bestboard = i.board
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
    return (bestVal, bestboard, minDepth)