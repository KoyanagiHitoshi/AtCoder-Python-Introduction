N = int(input())
takahashi, aoki = 0, 0
for i in range(N):
    X, Y = map(int, input().split())
    takahashi += X
    aoki += Y
if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
