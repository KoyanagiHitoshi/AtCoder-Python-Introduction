A, B, C, D = map(int, input().split())
print("Takahashi" if A < C else "Aoki" if A >
      C else "Takahashi" if B <= D else "Aoki")
