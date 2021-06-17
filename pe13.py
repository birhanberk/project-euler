# Problem 13 Large sum

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

with open("deneme.txt","r") as dosya:
    liste = dosya.readlines()
    toplam = 0
    dizi = []
    for i in range(0, 100):
        toplam += int(liste[i])
    for k in str(toplam):
        if(len(dizi) < 10):
            dizi.append(int(k))
    print(dizi)
