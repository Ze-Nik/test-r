gr = {
      '1': set(['2', '3', '4', '5']),
      '2': set(['1', '6', '7']),
      '3': set(['1', '8', '9']),
      '4': set(['1']),
      '5': set(['1']),
      '6': set(['2']),
      '7': set(['2']),
      '8': set(['3']),
      '9': set(['3'])}
m = []
q = []

def bfs(g, s, vis=[],):
    if s in vis:
        return vis
    vis.append(s)
    m.append(s)
    for v in g[s]:
        if v not in vis:
            q.append(v)
    while q:
        bfs(g, q.pop(0), vis)


print(bfs(gr, '1'))
