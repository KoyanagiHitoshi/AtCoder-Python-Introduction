V, A, B, C = map(int, input().split())
V = V % (A+B+C)
if V-A < 0:
    print("F")
elif V-(A+B) < 0:
    print("M")
else:
    print("T")
