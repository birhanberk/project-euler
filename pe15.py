def faktoriyel(sayi):
  if(sayi==1):
    return 1
  return sayi * faktoriyel(sayi-1)

sonuc = faktoriyel(40) / (faktoriyel(20) * faktoriyel(20))
print(sonuc)