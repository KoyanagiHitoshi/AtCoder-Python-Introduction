N = int(input())
A = list(map(int, input().split()))
for a in A:
    if a % 2 == 0:
        print(a, end=" ")
