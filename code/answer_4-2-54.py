S = input()
print("No" if "L" in S[::2] or "R" in S[1::2] else "Yes")
