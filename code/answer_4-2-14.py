N = int(input())
X, Y = 0, 0
for i in range(N):
    x, y = map(int, input().split())
    X += x
    Y += y
if X > Y:
    print("Takahashi")
elif X < Y:
    print("Aoki")
else:
    print("Draw")
