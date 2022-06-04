X = int(input())
print(40-X if 0 <= X < 40 else 70-X if 40 <= X <
      70 else 90-X if 70 <= X < 90 else "expert")
