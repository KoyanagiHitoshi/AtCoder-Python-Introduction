R, G, B = map(int, input().split())
C = input()
if C == "Red":
    print(min(G, B))
if C == "Green":
    print(min(R, B))
if C == "Blue":
    print(min(R, G))
