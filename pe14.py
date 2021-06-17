# Problem 14 Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

x = 2
sayac = 1
enbuyuk = 1
hafiza = 0
for i in range(x, 1000000):
    hafiza = i
    while True:
        if(i == 1):
            break
        elif(i % 2 == 0):
            i = int(i / 2)
            sayac += 1
        elif(i % 2 == 1):
            i = int((i * 3) + 1)
            sayac += 1
    if(enbuyuk < sayac):
        enbuyuk = sayac
    sayac = 0
print(enbuyuk)
