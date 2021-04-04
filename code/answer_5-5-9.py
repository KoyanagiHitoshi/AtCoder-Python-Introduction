A, B = input().split()
a = sum(map(int, A))
b = sum(map(int, B))
print(a if a > b else b)
