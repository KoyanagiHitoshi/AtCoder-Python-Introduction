N = int(input())
S = input()
count = 0
for i in range(1, N-1):
    if S[i-1:i+2] == "#.#":
        count += 1
print(count)
