N = int(input())
H = list(map(int, input().split()))
bridge = 0
for h in H:
    if h > bridge:
        bridge = h
print(H.index(bridge)+1)
