S = input()
if S[0] == S[1]:
    majority = S[0]
else:
    majority = S[2]
for i in range(len(S)):
    if S[i] != majority:
        print(i+1)
        break
