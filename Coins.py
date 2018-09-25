A = int(input())
B = int(input())
C = int(input())
X = int(input())

ptn = 0
for nA in range(A + 1):
  for nB in range(B + 1):
    for nC in range(C + 1):
      if 500*nA + 100*nB + 50*nC == X:
        ptn += 1

print(ptn)