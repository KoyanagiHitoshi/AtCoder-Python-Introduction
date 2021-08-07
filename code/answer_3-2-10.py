X = int(input())
year = 0
deposit = 100
while deposit < X:
    deposit = deposit*101//100
    year = year+1
print(year)
