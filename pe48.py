toplam = 0
for i in range(1, 1001):
  a = i ** i
  toplam += a
b = toplam % (10 ** 10)
print(b)