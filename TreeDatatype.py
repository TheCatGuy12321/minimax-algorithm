class Node:
    def __init__(self, data = None, board:tuple=None) -> None:
        self.data = data
        self.board = board
        self.children = []