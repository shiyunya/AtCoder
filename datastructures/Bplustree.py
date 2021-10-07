from collections import deque
import bisect
 
MAX = 256
 
class Node:
    def __init__(self, parent=None, brother=None, key=-float("inf")):
        self.isLeaf = False
        self.parent = parent
        self.keys = []
        self.brother = brother
        self.cnt = 0
        self.first = key
 
    def update(self):
        self.first = self.keys[0]
        self.cnt = len(self.keys)
 
    def search(self, key):
        ok = 0
        ng = self.cnt
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if self.keys[mid] <= key:
                ok = mid
            else:
                ng = mid
 
        return ok
 
class innerNode(Node):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.children = []
 
    def split(self):
        half = self.cnt // 2
 
        left = self
        right = innerNode()
 
        left_keys = self.keys[:half]
        right_keys = self.keys[half:]
        left_chidlren = self.children[:half]
        right_chidlren = self.children[half:]
 
        if self.parent is None:
            # Node is root
            self.__init__()
 
            left = innerNode()
            left.children = left_chidlren
            left.keys = left_keys
            left.update()
            for child in left.children:
                child.parent = left
 
            right.children = right_chidlren
            right.keys = right_keys
            right.update()
            for child in right.children:
                child.parent = right
 
            self.add(left)
            self.add(right)
            self.update()
 
        else:
            self.keys = left_keys
            self.children = left_chidlren
            self.update()
 
            right.keys = right_keys
            right.children = right_chidlren
            right.update()
            for child in right.children:
                child.parent = right
            self.parent.add(right)
 
        return left, right
 
    def merge(self):
        return
 
    def add(self, child):
        if self.cnt == MAX:
            left, right = self.split()
            if child.first < right.first:
                left.add(child)
            else:
                right.add(child)
        else:
            key = child.first
            idx = bisect.bisect_left(self.keys, key)
            self.keys.insert(idx, key)
            self.children.insert(idx, child)
            self.update()
            child.parent = self
 
        return
 
class leafNode(Node):
    def __init__(self, parent=None, brother=None, key=-float("inf")):
        super().__init__(parent=parent, brother=brother, key=key)
        self.isLeaf = True
        self.values = []
 
    def split(self):
        half = MAX // 2
        left_keys = self.keys[:half]
        right_keys = self.keys[half:]
        left_values = self.values[:half]
        right_values = self.values[half:]
 
        self.keys = left_keys
        self.values = left_values
        self.update()
 
        right = leafNode(brother=self.brother)
        right.keys = right_keys
        right.values = right_values
        right.update()
 
        self.brother = right
        self.parent.add(right)
 
        return
 
    def add(self, key, value=None, idx=-1):
        if self.cnt == MAX:
            self.split()
            if self.brother.first <= key:
                self.brother.add(key, value)
            else:
                self.add(key, value)
        else:
            if idx < 0:
                idx = bisect.bisect_left(self.keys, key)
            self.keys.insert(idx, key)
            self.values.insert(idx, value)
            self.update()
        return
 
    def upsert(self, key, value=None):
        idx = bisect.bisect_left(self.keys, key)
 
        if self.cnt > idx and self.keys[idx] == key:
            self.values[idx] = value
        else:
            self.add(key, value, idx)
 
    def delete(self, key):
        idx = bisect.bisect_left(self.keys, key)
 
        if self.cnt > idx and self.keys[idx] == key:
            self.keys.pop(idx)
            self.values.pop(idx)
            self.update()
 
    def predecessor(self, key):
        idx = self.search(key)
        return (self.keys[idx], self.values[idx])
 
    def successor(self, key):
        idx = self.search(key)
        if idx == self.cnt - 1:
            self = self.brother
            idx = 0
        else:
            idx += 1
        return (self.keys[idx], self.values[idx])
 
class Bplustree:
    def __init__(self, key=-float("inf")):
        root = innerNode()
        self.root = root
        leaf = leafNode(key=key)
        leaf.parent = root
        self.root.add(leaf)
 
    def getLeaf(self, key):
        now = self.root
        while not now.isLeaf:
            idx = now.search(key)
            now = now.children[idx]
        return now
 
    def add(self, key, value=None):
        now = self.getLeaf(key)
        now.add(key, value)
 
    def upsert(self, key, value=None):
        now = self.getLeaf(key)
        now.upsert(key, value)
 
    def delete(self, key):
        now = self.getLeaf(key)
        now.delete(key)
 
    def predecessor(self, key):
        now = self.getLeaf(key)
        return now.predecessor(key)
    
    def successor(self, key):
        now = self.getLeaf(key)
        return now.successor(key)
 
    def range(self, first, end):
        now = self.getLeaf(first)
        ans = []
 
        while now.first <= end:
            for i in range(now.cnt):
                if now.keys[i] < first:
                    continue
                if now.keys[i] <= end:
                    ans.append((now.keys[i], now.values[i]))
                else:
                    break
            else:
                if now.brother is not None:
                    now = now.brother
                    continue
                else:
                    break
            break
 
        return ans
 
    def print(self):
        print("-" * 10, "B+tree", "-" * 10)
 
        q = deque([(self.root, 0)])
        now, level = q.popleft()
        print("LEVEL", level, "ROOT :", now.keys)
        for i in range(now.cnt):
            q.append((now.children[i], level + 1))
 
        while q:
            now, level = q.popleft()
            node_type = "LEAF" if now.isLeaf else "INNER"
            print("LEVEL", level, node_type + " :", now.keys)
 
            if now.isLeaf:
                continue
            for i in range(now.cnt):
                q.append((now.children[i], level + 1))


bt = Bplustree()

bt.upsert(10, 'hoge')
bt.upsert(100, 'fuga')
bt.upsert(1, 'hage')

bt.print()
print()

print(bt.predecessor(50))
print(bt.successor(50))
print(bt.range(10,100))