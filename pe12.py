import time
ti = time.time()
sayi = 1
artis = 1

def carpanSayisi(sayi):
  """carpan = 1
  for i in range(2, sayi + 1):
    if(sayi % i == 0):
      carpan += 1"""
  i = 2
  x = 0
  toplam = 1
  dizi=[]
  while(sayi != 1):
    if(sayi % i == 0):
      sayi = sayi / i
      x += 1
    else:
      if(x != 0):
        dizi.append(x + 1)
      x = 0
      i += 1
  dizi.append(x + 1)
  for j in dizi:
    toplam = toplam * j
  return toplam

while True:
  carpan = carpanSayisi(sayi)
  #print(sayi, artis, carpan)
  if(carpan >= 481):
    break
  artis += 1
  sayi += artis
print(sayi)
print ("Time taken(secs):", time.time() - ti)