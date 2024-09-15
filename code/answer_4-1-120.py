A, B = map(int, input().split())
X = {(1, 2), (2, 3), (4, 5), (5, 6), (7, 8), (8, 9)}
if (A, B) in X:
    print("Yes")
else:
    print("No")
