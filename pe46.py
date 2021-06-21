# Problem 46 Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def allprimes(n):
    primes = []
    for i in range(2, n + 1):
        primes.append(i)
    for x in range(0, int(n / 2) + 1):
        if(primes[x] != 0):
            for i in range(x + primes[x], n - 1, primes[x]):
                primes[i] = 0
    primes.sort()
    return(primes[primes.count(0):])

def bul(n):
  if(n in primes):
    return False
  for p in primes:
    prime = int(p)
    if(prime >= n):
      break
    for x in range(1, n):
      if(n < prime + 2 * pow(x, 2)):
        break
      if(n == (prime + 2 * pow(x, 2))):
        return False
  return True

primes = allprimes(10000)
for i in range(9, 10000, 2):
  if(bul(i)):
    print(i)
    break
