n = int(input())

l = [True]*(n+1)
l[0] = l[1] = False
for i in range(2,int(n**0.5)+1):
    if l[i]:
        for j in range(i*2,n+1,i):
            l[j] = False
#print(l)
if l[n]:
    print("Prime number")
else:
    print("Not prime")