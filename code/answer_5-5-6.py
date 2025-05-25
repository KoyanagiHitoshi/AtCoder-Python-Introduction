x, y = input().split()
group1 = {"1", "3", "5", "7", "8", "10", "12"}
group2 = {"4", "6", "9", "11"}
if {x, y} <= group1 or {x, y} <= group2:
    print("Yes")
else:
    print("No")
