# Problem 5 Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isprime(a):
    """bir sayýnýn asal olup olmadýðýný kontrol eden fonksiyon"""
    i = 3
    if(a < 2):
        return False
    if a != 2 and a % 2 == 0:
        return False
    while i <= a ** (1 / 2):
        if a % i == 0:
            return False
        i += 2
    return True

sayi = 1
for i in range(1, 20):
  if(isprime(i)):
    sayi *= i
for j in range(2, 21):
  if(sayi % j == 0):
    continue
  else:
    for k in range(2, j):
      if(j % k == 0):
        sayi *= k
        break
print(sayi)