N, D = map(int, input().split())
S = input()
a = 0
for s in S:
    if s == "@":
        a += 1
print(N-a+D)
