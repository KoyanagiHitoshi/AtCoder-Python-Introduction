N = input()
print("No" if int(N) % sum(map(int, N)) else "Yes")
