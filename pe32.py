dizi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
toplam = []

def pandigitalMi(sayi1,sayi2,sayi3):
  liste = []
  for i in str(sayi1):
    liste.append(int(i))
  for i in str(sayi2):
    liste.append(int(i))
  for i in str(sayi3):
    liste.append(int(i))
  liste2 = sorted(liste)
  if(dizi == liste2):
    return True
  return False

for i in range(1000,10000): # 1 x 4
  for j in dizi:
    carpim = i * j
    if(pandigitalMi(i, j, carpim)):
      print(i, j, carpim)
      toplam.append(carpim)

for i in range(10,100): # 2 x 3
  for j in range(100, 1000):
    carpim = i * j
    if(pandigitalMi(i, j, carpim)):
      print(j, i, carpim)
      toplam.append(carpim)

sonuc = 0
toplam2 = set(toplam)
for i in toplam2:
  sonuc += i
print(sonuc)