def faktoriyel(sayi):
  fak=1
  for i in range(1,sayi+1):
    fak=fak*i
  return(fak)

def kombinasyon(n,r):
  kom=faktoriyel(n)//(faktoriyel(r)*(faktoriyel(n-r)))
  return(kom)
sayac=0
for i in range(1,101):
  for j in range(1,i+1):
    a=kombinasyon(i,j)
    if(a>1000000):
      sayac+=1
print(sayac)
