# Problem 36 Double-base palindromes

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def palindromMu(dizi):
  if(dizi == dizi[::-1]):
    return True
  return False

toplam = 0
for i in range(1, 1000000):
  dizi = []
  for j in str(i):
    dizi.append(j)
  if(palindromMu(dizi)):
    ikili = []
    h = i
    while h > 0:
      ikili.append(h % 2)
      h = int(h / 2)
    if(palindromMu(ikili)):
      toplam += i
print(toplam)
