N = int(input())
W = set(input().split())
S = {"and", "not", "that", "the", "you"}
if S & W:
    print("Yes")
else:
    print("No")
