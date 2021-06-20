# Problem 16 Power digit sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

toplam = 0
kuvveti = 2 ** 1000
for i in str(kuvveti):
  toplam = toplam + int(i)
print(toplam)
