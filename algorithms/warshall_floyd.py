inf = float('inf')

def warshall_floyd(way):
    n = len(way)
    f = [[[inf] * n for i in range(n)] for j in range(n + 1)]
    for s in range(n):
        for t in range(n):
            if (s == t):
                f[0][s][t] = 0
                continue
            for to,dis in way[s]:
                if t == to:
                    f[0][s][t] = dis
                    break     
    for k in range(n):
        for s in range(n):
            for t in range(n):
                f[k + 1][s][t] = min(f[k][s][t], f[k][s][k] + f[k][k][t])
    return f[n]

def warshall_floyd2(n, edge):
    f = [[inf] * n for i in range(n)]
    for i in range(n):
        f[i][i] = 0
    for source, distination, distance in edge:
        f[source][distination] = distance
    for k in range(n):
        for s in range(n):
            for t in range(n):
                f[s][t] = min(f[s][t], f[s][k] + f[k][t])
    return f

way = [[(1,2),(2,5)],[(2,1)],[]]
edge = [[0, 1, 2], [0, 2, 5], [1, 2, 1]]

print(warshall_floyd(way))
print(warshall_floyd2(3, edge))