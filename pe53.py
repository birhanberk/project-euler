# Problem 53 Combinatoric selections

# https://projecteuler.net/problem=53

def faktoriyel(n):
  toplam = 1
  for a in range(1, n + 1):
    toplam *= a;
  return toplam

def kombinasyon(n, r):
  return faktoriyel(n) // (faktoriyel(r) * (faktoriyel(n - r)))

sayac = 0
for i in range(1, 101):
  for j in range(1, i + 1):
    a = kombinasyon(i, j)
    if(a > 1000000):
      sayac += 1
print(sayac)
