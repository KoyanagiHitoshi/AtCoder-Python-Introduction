AB, AC, BC = input().split()
if (AB == ">" and AC == "<") or (AC == ">" and AB == "<"):
    print("A")
elif (AB == "<" and BC == "<") or (BC == ">" and AB == ">"):
    print("B")
else:
    print("C")
