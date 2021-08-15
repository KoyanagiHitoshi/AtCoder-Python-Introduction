N, K = map(int, input().split())
p = list(map(int, input().split()))
print(sum(sorted(p)[:K]))
