class UnionFind():
    par = []
    rank = []
    def __init__(self,n):
        for i in range(n):
            self.par.append(i)
            self.rank.append(0)
    def root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
 
    def same(self,x,y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False
 
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def comp(self):#rootまでの距離圧縮
        for i in range(len(self.par)):
            self.root(i)

#### Grid空間のUnionFind
class UnionFindGrid():
    par = []
    rank = []
    def __init__(self,h,w):
        for i in range(h):
            self.par.append([])
            self.rank.append([])
            for j in range(w):
                self.par[i].append((i,j))
                self.rank[i].append(0)
    def root(self,ij):
        i,j = ij
        if self.par[i][j] == (i,j):
            return (i,j)
        else:
            self.par[i][j] = self.root(self.par[i][j])
            return self.par[i][j]
 
    def same(self,ij,ij2):
        if self.root(ij) == self.root(ij2):
            return True
        else:
            return False
 
    def unite(self,ij,ij2):
        ij = self.root(ij)
        ij2 = self.root(ij2)
        if ij == ij2:
            return
        i,j = ij
        i2,j2 = ij2
        if self.rank[i][j] > self.rank[i2][j2]:
            self.par[i2][j2] = ij
        else:
            self.par[i][j] = ij2
            if self.rank[i][j] == self.rank[i2][j2]:
                self.rank[i2][j2] += 1

    def comp(self):#rootまでの距離圧縮
        for i in range(len(self.par)):
            for j in range(len(self.par[i])):
                self.root((i,j))