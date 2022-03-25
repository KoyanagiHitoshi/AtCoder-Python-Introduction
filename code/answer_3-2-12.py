N, K = map(int, input().split())
digits = 0
while(N > 0):
    N = N//K
    digits = digits+1
print(digits)
