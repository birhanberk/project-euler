# Problem 20 Factorial digit sum

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def faktoriyel(sayi):
  if(sayi == 1):
    return 1
  return sayi * faktoriyel(sayi - 1)

toplam = 0
x = faktoriyel(100)
for i in str(x):
  toplam += int(i)
print(toplam)
