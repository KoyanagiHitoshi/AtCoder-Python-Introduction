N, K = map(int, input().split())
S = input()
print(S[:K-1]+S[K-1:K].lower()+S[K:])
