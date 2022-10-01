A, B = input().split()
a = sum(map(int, A))
b = sum(map(int, B))
if a > b:
    print(a)
else:
    print(b)
