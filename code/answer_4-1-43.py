import math
X, Y = map(int, input().split())
if Y-X > 0:
    print(math.ceil((Y-X)/10))
else:
    print(0)
