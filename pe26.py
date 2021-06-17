x=1
sayiadeti=1001**2
artis=2
toplam=1
i=0
while x<=sayiadeti:
  for i in range(0,4):
    x+=artis
    toplam+=x
  if(x==sayiadeti):
    break
  artis+=2
print(toplam)
