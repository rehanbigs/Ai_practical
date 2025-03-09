import random
import time
class node:
    def __init__(self, name, value=None, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right

def generatetree(depth, current="root"):
    if depth == 0:
        value = random.randint(1, 100)
        return node(current, value=value)
    leftchild = generatetree(depth - 1, current + "l")
    rightchild = generatetree(depth - 1, current + "r")
    return node(current, left=leftchild, right=rightchild)

def minimax(n, maxp):
    if n.left is None and n.right is None:
        return n.value, [f"{n.name}({n.value})"]
    if maxp:
        leftvalue, leftpath = minimax(n.left, False)
        rightvalue, rightpath = minimax(n.right, False)
        if leftvalue >= rightvalue:
            bestvalue = leftvalue
            bestpath = [f"{n.name}(max)"] + leftpath
        else:
            bestvalue = rightvalue
            bestpath = [f"{n.name}(max)"] + rightpath
    else:
        leftvalue, leftpath = minimax(n.left, True)
        rightvalue, rightpath = minimax(n.right, True)
        if leftvalue <= rightvalue:
            bestvalue = leftvalue
            bestpath = [f"{n.name}(min)"] + leftpath
        else:
            bestvalue = rightvalue
            bestpath = [f"{n.name}(min)"] + rightpath
    return bestvalue, bestpath

treeroot = generatetree(10)
start = time.time()
optimalvalue, optimalpath = minimax(treeroot, True)
end = time.time()
print("Time taken: min max", end - start, "seconds")
print("optimal leaf node value:", optimalvalue)
print("path to optimal leaf node:")
print(" -> ".join(optimalpath))

def alphabeta(n,a,b, maxp):
    if n.left is None and n.right is None:
        return n.value, [f"{n.name}({n.value})"]
    if maxp:
        value = float('-inf')
        bestpath = []
        leftvalue, leftpath = alphabeta(n.left, a, b, False)
        if leftvalue > value:
            value = leftvalue
            bestpath = [f"{n.name}(max)"] + leftpath
        a = max(a, value)
        if b <= a:
            return value, bestpath
        rightvalue, rightpath = alphabeta(n.right, a, b, False)
        if rightvalue > value:
            value = rightvalue
            bestpath = [f"{n.name}(max)"] + rightpath
        a = max(a, value)
        return value, bestpath
    else:
        value = float('inf')
        bestpath = []
        leftvalue, leftpath = alphabeta(n.left, a, b, True)
        if leftvalue < value:
            value = leftvalue
            bestpath = [f"{n.name}(min)"] + leftpath
        b = min(b, value)
        if b <= a:
            return value, bestpath
        rightvalue, rightpath = alphabeta(n.right, a, b, True)
        if rightvalue < value:
            value = rightvalue
            bestpath = [f"{n.name}(min)"] + rightpath
        b = min(b, value)
        return value, bestpath



treeroot = generatetree(10)
start=time.time()
optimalvalue, optimalpath = alphabeta(treeroot, float('-inf'), float('inf'), True)
end = time.time()
print("Time taken:alpha beta", end - start, "seconds")
print("optimal leaf node value:", optimalvalue)
print("path to optimal leaf node:")
print(" -> ".join(optimalpath))
