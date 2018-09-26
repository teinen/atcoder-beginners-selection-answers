import sys

def findSumOfDigits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

def main():
  IN = [int(_) for _ in input().split()]
  N, A, B = IN[0], IN[1], IN[2]
  t = 0
  for i in range(N + 1):
    sum = findSumOfDigits(i)
    if sum >= A and sum <= B:
      t += i
  print(t)


main()
