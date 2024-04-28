N = int(input())
W = set(input().split())
S = {"and", "not", "that", "the", "you"}
print("Yes" if S & W else "No")
