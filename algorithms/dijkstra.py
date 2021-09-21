import heapq

def dijkstra(graph, start, goal):
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, (0, start))
    isVisit = [False] * len(graph)
    distances = [-1] * len(graph)

    while hq:
        dist_start_now, now = heapq.heappop(hq)
        if isVisit[now]:
            continue

        isVisit[now] = True
        distances[now] = dist_start_now
        
        if now == goal:
            break

        for next, dist_now_next in graph[now]:
            heapq.heappush(hq, (dist_start_now + dist_now_next, next))
            
    else:
        return -1

    return dist_start_now

graph = [[(1, 2), (2, 5)], [(2, 1)], []]

print(dijkstra(graph, 0, 2))