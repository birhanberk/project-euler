toplam=0
for i in range(1,2000000):
  liste=[]
  x=[]
  for j in str(i):
    liste.append(j)
    x.append(j)
  liste.reverse()
  y=liste
  if(x==y):
    ikili=[]
    a=[]
    h=i
    while h>0:
      ikili.append(h%2)
      a.append(h%2)
      h=int(h/2)
    ikili.reverse()
    b=ikili
    if(a==b):
      print(i,a)
      toplam+=i
print(toplam)
