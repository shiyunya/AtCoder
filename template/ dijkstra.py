import heapq

def dijkstra(way,start,goal):
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq,(0,start))
    f = [False]*len(way)
    while hq:
        dis,e = heapq.heappop(hq)
        if f[e]:
            continue
        else:
            f[e] = True
        if e == goal:
            break
        for e2,t in way[e]:
            heapq.heappush(hq,(dis + t,e2))
    else:
        return -1
    return dis

way = [[(1,2),(2,5)],[(2,1)],[]]

print(dijkstra(way,0,2))