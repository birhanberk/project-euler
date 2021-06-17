# Problem 2 Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

n1 = 1
n2 = 2
toplam = 2
for i in range(1, 50):
  fib = n1 + n2
  n1 = n2
  n2 = fib
  if(fib % 2 == 0):
    if(fib > 4000000):
      break
    else:
      toplam = toplam + fib
print(toplam)
