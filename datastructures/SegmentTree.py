
class SegmentTree():

    def __init__(self, n, e = 0):
        self.size = 2 ** (n - 1).bit_length()
        self.tree = [e] * 2 * self.size
        self.e = e

    def operator(self, x, y):
        return max(x,y)

    def update(self, n, x):
        idx = self.size + n
        self.tree[idx] = x
        idx = idx //  2
        while idx > 0:
            self.tree[idx] = self.operator(self.tree[idx * 2], self.tree[idx * 2 + 1])
            idx = idx //  2

    def query(self, l, r):
        l += self.size
        r += self.size
        resl = self.e
        resr = self.e
        while l < r:
            if l % 2 == 1:
                resl = self.operator(resl, self.tree[l])
                l += 1
            if r % 2 == 1:
                resr = self.operator(resr, self.tree[r - 1])
                r -= 1
            l //= 2
            r //= 2
        return self.operator(resl, resr)
