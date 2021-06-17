# Problem 9 Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(200,500):
  for j in range(200,500):
    if(i>=j):
      continue
    for k in range(200,500):
      if(j>=k):
        continue
      if(i**2+j**2==k**2):
        if(i+j+k==1000):
          print(i,j,k)
          print(i*j*k)
