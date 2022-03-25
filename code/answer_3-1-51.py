S1 = input()
S2 = input()
print("No" if (S1 == "#." and S2 == ".#") or (
    S1 == ".#" and S2 == "#.") else "Yes")
