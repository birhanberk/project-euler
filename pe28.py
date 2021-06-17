x=1
artis=2
toplam=1
sayi=1001*1001
while True:
  for i in range(0,4):
    x+=artis
    toplam+=x
  artis+=2
  if(x>=sayi):
    break
print(toplam)
