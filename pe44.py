"""pentagon = []
for n in range(1,1000):
  pentagon.append(n*(3*n-1)//2)

def bul(i, j):
  toplam = pentagon[i] + pentagon[j]
  fark = pentagon[j] - pentagon[i]
  if(fark in pentagon):
    print(pentagon[i],pentagon[j],toplam)
  if(toplam in pentagon and fark in pentagon):
    print(pentagon[i],pentagon[j],toplam,fark)
    return True
  return False
#print(pentagon)
for i in range(0, 1000):
  for j in range(i+1, 999):
    #print(pentagon[i],pentagon[j])
    if(bul(i, j)):
      print(i, j,"bulduk")
"""
def pentagonalmi(n):
  if (1+(24*n+1)**0.5) % 6 == 0:
    return True
  return False

kontrol = True
i = 1
while kontrol:
  for j in range(1, i):
    a = i*(3*i-1)/2
    b = j*(3*j-1)/2
    if pentagonalmi(a+b) and pentagonalmi(a-b):
      print((int)(a-b))
      kontrol = False
      break
  i += 1