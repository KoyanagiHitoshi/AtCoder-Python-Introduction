N = int(input())
S = [input() for i in range(N)]
print(*S[::-1], sep="\n")
