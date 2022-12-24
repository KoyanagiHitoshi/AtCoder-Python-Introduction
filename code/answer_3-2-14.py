a, b, n = [int(input()) for i in range(3)]
while n % a != 0 or n % b != 0:
    n = n+1
print(n)
