A, B, K = map(int, input().split())
print(A-K, B) if K <= A else print(0, B-(K-A)) if K <= A+B else print(0, 0)
