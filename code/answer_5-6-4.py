R, C = map(int, input().split())
print("black" if max(abs(R-8), abs(C-8)) % 2 == 1 else "white")
