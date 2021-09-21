
class SCC():
    def __init__(self,n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.rgraph = [[] for i in range(n)]
        self.isVisit = [False] * n
        self.componets = [-1] * n
        self.order = []
        #self.scc = []

    def dfs(self,now):
        if self.isVisit[now] :
            return
        self.isVisit[now] = True
        for to in self.graph[now]:
            self.dfs(to)
        self.order.append(now)
        return     

    def rdfs(self,now,cnt):
        if self.isVisit[now] :
            return
        self.isVisit[now] = True
        for to in self.rgraph[now]:
            self.rdfs(to,cnt)
        self.componets[now] = cnt
    
    def clearFlag(self):
        self.isVisit = [False] * self.n

    def build(self):
        for i in range(self.n):
            self.dfs(i)
        self.clearFlag()
        for i in range(self.n)[::-1]:
            self.rdfs(self.order[i],self.n - i - 1)