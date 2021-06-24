# Problem 34 Digit factorials

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def faktoriyel(n):
  toplam = 1
  for a in range(1, n + 1):
    toplam *= a;
  return toplam

t = 0
for i in range(3, 50000):
  s = 0
  for j in str(i):
    s += faktoriyel(int(j))
  if(s == i):
    t += s
print(t)
