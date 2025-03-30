A, B = map(int, input().split())
s = {1, 2, 3}
s.discard(A)
s.discard(B)
if A == B:
    print(-1)
else:
    print(s.pop())
