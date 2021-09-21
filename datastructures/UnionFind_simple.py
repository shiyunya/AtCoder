class UnionFind():
    par = []
    def __init__(self,n):
        for i in range(n):
            self.par.append(i)
 
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
        self.par[y] = x
    
    def comp(self):#rootまでの距離圧縮
        for i in range(len(self.par)):
            self.root(i)