from collections import deque

def topological_sort(graph):
    n = len(graph)
    IN = [0] * n
    ret = []
    isVisit = [False] * n

    for i in range(n):
        for j in range(len(graph[i])):
            IN[graph[i][j]] += 1

    q = deque([])
    for i in range(n):
        if IN[i] == 0:
            q.append(i)
            
    while q :
        now = q.pop()
        ret.append(now)
        for to in graph[now]:
            IN[to] -= 1
            if IN[to] == 0:
                q.append(to)

    if len(ret) != len(graph):
        # NOT DAG
        return -1, ret

    return 0, ret

graph = [[1, 2], [2], []]

print(topological_sort(graph))