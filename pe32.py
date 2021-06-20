# Problem 32 Pandigital products

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
toplam = []

def pandigitalMi(s1, s2, s3):
  a = []
  for i in str(s1):
    a.append(int(i))
  for i in str(s2):
    a.append(int(i))
  for i in str(s3):
    a.append(int(i))
  a2 = sorted(liste)
  if(a == a2):
    return True
  return False

def islem(i, j):
    carpim = i * j
    if(pandigitalMi(i, j, carpim)):
      toplam.append(carpim)

for i in range(1000,10000): # 1 x 4
  for j in dizi:
    islem(i, j)

for i in range(10,100): # 2 x 3
  for j in range(100, 1000):
    islem(i, j)

sonuc = 0
toplam2 = set(toplam)
for i in toplam2:
  sonuc += i
print(sonuc)
