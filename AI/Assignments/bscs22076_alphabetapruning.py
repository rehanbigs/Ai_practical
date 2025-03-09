tree = {
    "A": ["B", "C"],
    "B": ["D", "E", "F"],
    "C": ["G", "H", "I"],
    "D": ["J", "K"],
    "E": ["L", "M"],
    "F": ["N", "O"],
    "G": ["P", "Q"],
    "H": ["R", "S"],

    "I": ["T", "U"],
    
    "J": 10,
    "K": 20,
    "L": 30,
    "M": 15,
    "N": 15,
    "O": 30,
    "P": 25,
    "Q": 35,
    "R": 5,
    "S": 10,
    "T": 35,
    "U": 40
}

def alphabeta(n,a,b,maxflag):
    if not isinstance(tree[n],list):
        return tree[n]
    if maxflag:
        cur=float('-inf')
        for ch in tree[n]:
            temp=alphabeta(ch,a,b,False)
            cur=max(cur,temp)
            a= max(a,cur)
            if b<=a:
                break
        return cur
    else:
        cur =float('inf')
        for ch in tree[n]:
            temp= alphabeta(ch,a,b,True)
            cur = min(cur,temp)
            b =min(b,cur)
            if b <= a:
                break
        return cur

res=alphabeta("A", float('-inf'), float('inf'), True)
print("optimal value for node Ais:", res)
