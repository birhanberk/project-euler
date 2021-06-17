f1=1
f2=1
fib=2
i=2
while True:
  liste=[]
  fib=f1+f2
  f1=f2
  f2=fib
  i=i+1
  for j in str(fib):
    liste+=[j]
  if(len(liste)>=1000):
    print(i)
    break
