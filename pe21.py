def carpanbul(sayi):
  toplam=0
  for i in range(1,sayi):
    if(sayi%i==0):
      toplam+=i
  return(toplam)
toplam2=0
for j in range(1,10000):
  a=carpanbul(j)
  x=carpanbul(a)
  if(j==x and x!=a):
    toplam2+=j
print(toplam2)
