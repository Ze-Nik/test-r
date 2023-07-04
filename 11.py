inc = {
    1: [2, 3, 4, 5],
    2: [1, 6, 7],
    3: [1, 8, 9],
    4: [1],
    5: [1],
    6: [2],
    7: [2],
    8: [3],
    9: [3]}


visited = set()
Q = []
BFS = []


def bfs(v):
    if v in visited:
        return
    visited.add(v)
    BFS.append(v)
    for i in inc[v]:
        if i not in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))

bfs(1)
print(BFS)