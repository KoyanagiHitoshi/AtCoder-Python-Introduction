S = input()
N = len(set(S))
print(1 if N == 1 else 3 if N == 2 else 6)
