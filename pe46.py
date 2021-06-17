f = open("primes-to-100k.txt", "r")
lines = f.read().split("\n")
f.close()

# n = p + 2 * pow(x, 2)
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2

def bul(n):
  if(str(n) in lines):
    return False
  for p in lines:
    prime = int(p)
    if(prime >= n):
      break
    for x in range(1, n):
      if(n < prime + 2 * pow(x, 2)):
        break
      if(n == (prime + 2 * pow(x, 2))):
        return False
  return True

for i in range(9,10000,2):
  if(bul(i)):
    print(i)
    break