N, X = map(int, input().split())
S = list(map(int, input().split()))
total = 0
for s in S:
    if s <= X:
        total += s
print(total)
