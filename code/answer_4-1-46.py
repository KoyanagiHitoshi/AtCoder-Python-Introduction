A, B = map(int, input().split())
if A == B:
    print(1)
elif (A-B) % 2 == 1:
    print(2)
else:
    print(3)
