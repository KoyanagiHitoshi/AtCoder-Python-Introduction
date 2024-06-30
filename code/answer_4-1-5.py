A, B = map(int, input().split())
if A == B:
    print(-1)
if A == 1 and B == 2:
    print(3)
if A == 1 and B == 3:
    print(2)
if A == 2 and B == 1:
    print(3)
if A == 2 and B == 3:
    print(1)
if A == 3 and B == 1:
    print(2)
if A == 3 and B == 2:
    print(1)
