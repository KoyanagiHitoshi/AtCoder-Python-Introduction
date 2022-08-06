a, b = map(int, input().split())
print("Yes" if a == b-1 or (a == 1 and b == 10) else "No")
