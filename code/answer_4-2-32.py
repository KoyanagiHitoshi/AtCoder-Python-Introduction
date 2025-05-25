N = int(input())
W = input().split()
S = {"and", "not", "that", "the", "you"}
for w in W:
    if w in S:
        print("Yes")
        break
else:
    print("No")
