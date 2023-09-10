import math
N, M, P = map(int, input().split())
print(max(0, math.ceil((N-M+1)/P)))
