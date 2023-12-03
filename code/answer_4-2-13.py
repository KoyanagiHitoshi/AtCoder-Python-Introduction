N = int(input())
salary = 0
for i in range(1, N+1):
    salary += i*10000*(1/N)
print(salary)
