# Problem 10 Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

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
