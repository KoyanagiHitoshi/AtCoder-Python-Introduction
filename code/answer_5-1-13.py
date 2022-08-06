N = int(input())
ST = [input() for i in range(N)]
print("Yes" if len(set(ST)) < N else "No")
