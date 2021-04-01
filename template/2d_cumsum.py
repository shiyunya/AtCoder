# 2次元累積和 ABC106 D 参照

def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy as np
import sys
sys.setrecursionlimit(2147483647)
import math
from itertools import accumulate
from itertools import permutations
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import heapq
inf = float('inf')
dic = defaultdict(lambda:0)

n,m,q = L()
lr = NL(m)
pq = NL(q)

train = [[0]*(n+1) for i in range(n+1)]

for l,r in lr:
    train[l][r] += 1

for i in range(1,n+1):
    for j in range(1,n+1):
        train[i][j] += train[i-1][j] + train[i][j-1] - train[i-1][j-1]

for p,q in pq:
    #print(p,q)
    ans = train[q][q] - train[q][p-1] - train[p-1][q] + train[p-1][p-1]
    print(ans)