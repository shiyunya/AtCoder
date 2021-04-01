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
from decimal import Decimal
from itertools import product
inf = float('inf')
dic = defaultdict(lambda:0)

h,w = list(map(int,input().split()))
maze = []
for i in range(h):
    maze.append(input())

d = 'e'
q = deque([])
q.append((0,0))

def check_east(i,j):
    if j < w-1:
        if maze[i][j+1] == ".":
            global d
            d = 'e'
            q.append((i,j+1))
            return True
    return False

def check_south(i,j):
    if i < h-1:
        if maze[i+1][j] == ".":
            global d
            d = 's'
            q.append((i+1,j))
            return True
    return False

def check_west(i,j):
    if j > 0:
        if maze[i][j-1] == ".":
            global d
            d = 'w'
            q.append((i,j-1))
            return True
    return False

def check_north(i,j):
    if i > 0:
        if maze[i-1][j] == ".":
            global d
            d = 'n'
            q.append((i-1,j))
            return True
    return False

while q:
    i,j = q.popleft()
    maze[i] = maze[i][:j] + "#" + maze[i][j+1:]
    print("\n".join(maze))
    print("------------")
    if d == 'e':
        # s
        if check_east(i,j):
            continue         
        # r
        if check_south(i,j):
            continue
        # l
        if check_north(i,j):
            continue
    elif d == "s":
        # s        
        if check_south(i,j):
            continue
        # r
        if check_west(i,j):
            continue
        # l
        if check_east(i,j):
            continue
    elif d == "w":
        # s        
        if check_west(i,j):
            continue
        # r
        if check_north(i,j):
            continue
        # l
        if check_south(i,j):
            continue
    else:
        # s        
        if check_north(i,j):
            continue
        # r
        if check_east(i,j):
            continue
        # l
        if check_west(i,j):
            continue
print(j,i)