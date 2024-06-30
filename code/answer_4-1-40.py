X, A, B = map(int, input().split())
if X < B-A:
    print("dangerous")
elif A < B:
    print("safe")
else:
    print("delicious")
