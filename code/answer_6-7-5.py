N, X = map(int, input().split())
string = ""
for i in range(26):
    for j in range(N):
        string = string+chr(ord("A")+i)
print(string[X-1])
