N, A, B = map(int, input().split())
C = list(map(int, input().split()))
idx = 1
for c in C:
    if A+B == c:
        print(idx)
    else:
        idx += 1
