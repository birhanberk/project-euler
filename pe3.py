# Problem 3 Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def allprimes(n):
  """bir sayýdan küçük bütün asal sayýlarý dizi olarak döndüren fonksiyon"""
  primes=[]
  for i in range(2, n + 1):
    primes.append(i)
  for x in range(0, int(n / 2) + 1):
    if(primes[x] != 0):
      for i in range(x + primes[x], n - 1, primes[x]):
        primes[i] = 0
  primes.sort()
  return(primes[primes.count(0):])

primes = allprimes(10000)
n = 600851475143
sonuc = 0
for i in primes:
  if(n % i == 0):
    sonuc = i
print(sonuc)