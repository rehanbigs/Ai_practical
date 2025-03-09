
import heapq


def astar(start, goal, graph, heur):
    openlist = []
    heapq.heappush(openlist, (heur[start], 0, start, [start]))
    closed = set()
    while openlist:
        f, g, node, path = heapq.heappop(openlist)
        if node == goal:
            return path
        if node in closed:
            continue
        closed.add(node)
        
        for neigh in graph.get(node, {}):
            if neigh in closed:
                continue
            cost = graph[node][neigh]
            newg = g + cost
            newf = newg + heur[neigh]
            newpath = path + [neigh]
            heapq.heappush(openlist, (newf, newg, neigh, newpath))
    return None

# graph and heuristic estimates
graph = {
    'a': {'b': 1, 'c': 3},
    
    'b': {'d': 2},
    'c': {'d': 1, 'e': 5},
    'd': {'z': 1},
    'e': {'z': 1},
    'z': {}
}


heur = {
    'a': 5,
    'b': 4,
    'c': 3,
    'd': 2,
    'e': 1,
    'z': 0
}


path = astar('a', 'z', graph, heur)
print("Path found:", path)
