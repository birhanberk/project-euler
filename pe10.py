"""
x=0
toplam=2
for i in range(3,2000000,2):
  x=0
  for j in range(3,i,2):
    if(j**2<=i):
      if(i%j==0):
        x+=1
        if(x<=1):
          break
    else:
      break
  if(x==0):
    toplam+=i
print(toplam)
"""
"""
dizi = [0] * 2000000
asal = 3
toplam = 2
while asal < 2000000:
    if dizi[asal] == 0:
        toplam += asal
        i = asal
        while i < 2000000:
            dizi[i] = 1
            i += asal
    asal += 2
print(toplam)
"""

def allprimes(n):
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])
  
print(sum(allprimes(2000000)))