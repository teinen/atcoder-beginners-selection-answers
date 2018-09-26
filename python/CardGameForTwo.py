N = int(input())
A = sorted([int(_) for _ in input().split()], reverse=True)
Alice = 0
Bob = 0
for i, a in enumerate(A):
  if i % 2 == 0:
    Alice += a
  else:
    Bob += a
print(Alice - Bob)
