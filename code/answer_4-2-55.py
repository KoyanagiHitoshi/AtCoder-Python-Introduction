K = int(input())
S = input()
print(S[:K]+"..." if len(S) > K else S)
