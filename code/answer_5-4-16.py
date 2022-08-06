N, A, B = map(int, input().split())
div = N//(A+B)
mod = N % (A+B)
print(div*A+min(mod, A))
