N = int(input())
k = 0
while 2**k <= N:
    k = k+1
print(k-1)
