import math
X, Y = map(int, input().split())
print(max(0, math.ceil((Y-X)/10)))
