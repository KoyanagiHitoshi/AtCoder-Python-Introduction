A, B, C = map(int, input().split())
mod = B-(B % C)
if A <= mod:
    print(mod)
else:
    print(-1)
