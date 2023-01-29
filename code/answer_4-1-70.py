A, B = map(int, input().split())
if A == B:
    print("Draw")
elif (A+13) % 15 < (B+13) % 15:
    print("Bob")
else:
    print("Alice")
