toplam=0
ustsinir=5*(9**5)
for j in range(2,ustsinir):
  sayi=0
  for i in str(j):
    sayi+=int(i)**5
  if(j==sayi):
    toplam+=sayi
print(toplam)
