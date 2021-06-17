f = open("names.txt", "r")
for i in f:
  d = i.split(',')
f.close()

alphabet = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

def sirala(dizi):
  ndizi=[]
  for j in dizi:
    dizi = j.replace('"', "")
    ndizi.append(dizi)
  ndizi.sort()
  return ndizi

def hesapla(dizi):
  toplam = 0
  index = 1
  for i in dizi:
    isimToplami = 0
    araTop = 0
    for j in i:
      isimToplami += alphabet.get(j)
    araTop = isimToplami * index
    toplam = toplam + araTop
    index += 1
  return toplam

dizi = sirala(d)
print(hesapla(dizi))