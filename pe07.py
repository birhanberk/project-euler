def isprime(a):
  """bir sayýnýn asal olup olmadýðýný kontrol eden fonksiyon"""
  i = 3
  if(a < 2):
    return(0)
  if a != 2 and a % 2 == 0:
    return(0)
  while i <= a ** (1 / 2):
    if a % i == 0:
      return(0)
    i += 2
  return(1)

n = 0
p = 1
while n < 10001:
  p += 1
  if(isprime(p) == 1):
    n += 1
print(p)
