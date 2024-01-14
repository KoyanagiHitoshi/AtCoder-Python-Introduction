N = int(input())
S = input()
T = S.count("T")
A = S.count("A")
if T > A:
    print("T")
elif T < A:
    print("A")
else:
    if S[-1] == "A":
        print("T")
    else:
        print("A")
