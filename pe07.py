# Problem 7 10001st prime

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def isprime(a):
  # bir sayının asal olup olmadığını kontrol eden fonksiyon
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
