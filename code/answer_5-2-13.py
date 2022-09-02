N = int(input())
A = list(map(int, input().split()))
a = sorted(A)[-2]
print(A.index(a)+1)
