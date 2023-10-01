N = int(input())
S = [input() for i in range(N)]
if S.count("For") > N/2:
    print("Yes")
else:
    print("No")
