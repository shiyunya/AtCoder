n = int(input())

div = [1]*(n+1)#div[i] = iの約数の個数
div[0] = 0
for i in range(2,n+1):
    for j in range(i, n + 1, i):
        div[j] += 1

print(div)