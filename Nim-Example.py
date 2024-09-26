from minimax import Minimax, Node # import the minimax function and the Node data structure
from time import sleep


def get_tree(b, Myturn:bool):
    finished = True
    for i in b:
        if i != 0:
            finished = False
    if finished:
        if Myturn:
            return Node(-1, tuple(b)) # lost game
        else:
            return Node(1, tuple(b)) # won game
    
    ThisNode = Node(None, tuple(b))
    for i in range(len(b)):
        if b[i] == 0:
            continue
        for j in range(b[i]):
            _temp = list(b)
            _temp[i] = j
            tempv = get_tree(_temp, not(Myturn))
            ThisNode.children.append(tempv)
    return ThisNode

def draw_tree(rootnode: Node):
    print(rootnode.board, rootnode.data)
    for i in rootnode.children:
        draw_tree(i)

def calculate_position():
    root_node = get_tree(board, True)
    print("Generated tree, starting calculation")
    best_move = Minimax(root_node, True)[1]
    print("Finished calculation")
    return list(best_move)

def get_board():
    board = input("Board setup (seperated by spaces):  ").split(" ")
    board2 = []
    for i in range(len(board)):
        board2.append(int(board[i]))
    return board2

def get_player_choice():
    _list = input("Pick the pile and then the amount to take:  ").split(" ")
    player_choice = [0, 0]
    try:
        player_choice[0] = int(_list[0]) - 1
        player_choice[1] = int(_list[1])
    except:
        print("Please input integers")
        return get_player_choice()
    if player_choice[0]+1 > len(board):
        print("Please choose the batch again")
        return get_player_choice()
    if board[player_choice[0]] < player_choice[1]:
        print("Invalid number")
        return get_player_choice()
    if player_choice[1] <= 0:
        print("Please input a natural number")
        return get_player_choice()
    return player_choice

def P1_wins():
    print(board)
    print("Player 1 wins!")
    sleep(3)
    exit()

def P2_wins():
    print(board)
    print("Player 2 wins!")
    sleep(3)
    exit()

def update_board(_player_choice, P1_turn):
    board[_player_choice[0]] -= _player_choice[1]
    win = True
    for i in board:
        if i != 0:
            win = False
    if win and P1_turn:
        P1_wins()
    elif win and not(P1_turn):
        P2_wins()


def main():
    global board
    print("Starting Nim game")
    board = get_board()
    while True:
        print("P1")
        player_choice = get_player_choice()
        update_board(player_choice, True)
        for i in board:print(i, end=" ")
        print()
        
        print("P2")
        board = calculate_position()
        win = True
        for i in board:
            if i!=0:
                win = False
        if win:
            P2_wins()
        for i in board:print(i, end=" ")
        print()


if __name__ == '__main__':
    main()