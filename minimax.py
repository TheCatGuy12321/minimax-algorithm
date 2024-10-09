from TreeDatatype import Node # import modified Binary tree data structure, function only compatible with this
from math import inf

def Minimax(root: Node, Maximising: bool, depth=0, alpha=-inf, beta=inf):
    if len(root.children) == 0:
        return (root.data, root.board, depth)
    if Maximising: # Maximise
        data = []
        bestVal = -inf
        bestboard = []
        for i in root.children:
            temp = Minimax(i, not Maximising, depth+1, alpha, beta)
            data.append([temp[0], i.board, temp[2]])
            value = data[-1][0]
            if bestVal < value:
                bestVal = value
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        if bestVal > 0: # if winning
            bestDepth = inf
            for i in data:
                if i[0] == bestVal:
                    if bestDepth > i[2]: # minimise depth
                        bestboard = i[1]
                        bestDepth = i[2]
        else: # if losing
            bestDepth = -inf
            for i in data:
                if i[0] == bestVal: 
                    if bestDepth < i[2]: # maximise depth
                        bestboard = i[1]
                        bestDepth = i[2]
        return (bestVal, bestboard, bestDepth)
    
    else: # Minimise
        data = []
        bestVal = inf
        bestboard = []
        for i in root.children:
            temp = Minimax(i, not Maximising, depth+1, alpha, beta)
            data.append([temp[0], i.board, temp[2]])
            value = data[-1][0]
            if bestVal > value:
                bestVal = value
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        if bestVal <= 0: # if winning for opponent
            bestDepth = inf
            for i in data:
                if i[0] == bestVal:
                    if bestDepth > i[2]: # minimise depth
                        bestboard = i[1]
                        bestDepth = i[2]
        else: # if losing
            bestDepth = -inf
            for i in data:
                if i[0] == bestVal: 
                    if bestDepth < i[2]: # maximise depth
                        bestboard = i[1]
                        bestDepth = i[2]
        return (bestVal, bestboard, bestDepth)
