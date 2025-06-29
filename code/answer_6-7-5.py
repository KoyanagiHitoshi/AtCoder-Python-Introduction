S = input()
for i in range(26):
    if chr(i+ord("a")) not in S:
        print(chr(i+ord("a")))
        break
