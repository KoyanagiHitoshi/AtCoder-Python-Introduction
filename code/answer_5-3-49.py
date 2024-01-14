N = int(input())
S = input()
if S.find("|") < S.find("*") < S.rfind("|"):
    print("in")
else:
    print("out")
