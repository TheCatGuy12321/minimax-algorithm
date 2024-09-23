from minimax import Node # import the minimax function and the Node data structure
import minimax
import multiprocessing
a1 = Node(None)
b1 = Node(None)
b2 = Node(None)
c1 = Node(None)
c2 = Node(None)
c3 = Node(None)
c4 = Node(None)
d1 = Node(None)
d2 = Node(None)
d3 = Node(None)
d4 = Node(None)
d5 = Node(None)
d6 = Node(None)
e1 = Node(10)
e2 = Node(944)
e3 = Node(5)
e4 = Node(-10)
e5 = Node(7)
e6 = Node(5)
e7 = Node(-8336)
e8 = Node(-7)
e9 = Node(-5)
a1.children = [b1,b2]
b1.children = [c1,c2]
b2.children = [c3,c4]
c1.children = [d1,d2]
c2.children = [d3]
c3.children = [d4,d5]
c4.children = [d6]
d1.children = [e1,e2]
d2.children = [e3]
d3.children = [e4]
d4.children = [e5,e6]
d5.children = [e7]
d6.children = [e8,e9]

if __name__ == '__main__':
    import time
    begin = time.time()
    print(minimax.Minimax(a1, True))
    end = time.time()
    print(f"total time: {end-begin}") # only do threading with large trees!