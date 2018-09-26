IN = [int(_) for _ in input().split()]
N = IN[0]
Y = IN[1]
cnt10000, cnt5000, cnt1000 = -1, -1, -1
for a in range(N + 1):
  for b in range(N + 1 - a):
    c = N - a - b
    if 10000*a + 5000*b + 1000*c == Y:
      cnt10000, cnt5000, cnt1000 = a, b, c
print("{} {} {}".format(cnt10000, cnt5000, cnt1000))
