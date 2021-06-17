sayac=0
for i in range(1,10):
  for j in range(1,22):
    kuvvet=i**j
    if(len(str(kuvvet))==j):
      sayac+=1
print(sayac)
