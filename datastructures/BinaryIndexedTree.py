# 更新される数列の区間和を効率的に計算

class BinaryIndexedTree():
    bit = []
    size = 0
    def __init__(self,size):
        self.bit = [0]*(size+1)
        self.size = size

    def add(self,x,w):
        while x <= self.size:
            self.bit[x] += w
            x += x & -x
    
    def sum(self,a):
        ret = 0
        x = a
        while x > 0:
            ret += self.bit[x]
            x -= x & -x
        return ret
