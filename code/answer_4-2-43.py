N = int(input())
T = input()
A = input()
for i in range(N):
    if T[i] == A[i] == "o":
        print("Yes")
        break
else:
    print("No")
