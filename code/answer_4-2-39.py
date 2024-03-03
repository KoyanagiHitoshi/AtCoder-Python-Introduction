a, b, n = [int(input()) for i in range(3)]
while not (n % a == 0 and n % b == 0):
    n += 1
print(n)
