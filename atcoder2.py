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
import re
inf = float('inf')
dic = defaultdict(lambda:0)
from decimal import Decimal

s = input()
ints = int(s,2)
st = input()
t = int(st)
bint = int(st,2)
#print(3^1)
lent = len(st)
#print(lent)
ans = inf

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

seed = pow(2,lent) - 1
#print(bin(seed))
#print(len(s)-lent + 1)
for i in range(len(s) - lent + 1):
    #print(s[i:i+lent])
    #print(int(s[i:i+lent],2)^bint)
    #tmp = int(s[i:i + lent],2)
    
    tmp = (ints & seed<<i)>>i
    #print(bin(tmp))
    #print(tmp,bint)
    tans = popcount((tmp^bint))
    ans = min(ans,tans)
print(ans)