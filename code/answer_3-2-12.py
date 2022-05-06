N = int(input())
T = input()
x = 0
y = 0
dx = 1
dy = 0
for t in T:
    if t == "S":
        x = x+dx
        y = y+dy
    else:
        tmp = dx
        dx = dy
        dy = -tmp
print(x, y)
