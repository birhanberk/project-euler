kitaplik={0:"and",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"onethousand"}

def hesapla(i):
  if(i < 20):
    #print(i,len(kitaplik[i]))
    return len(kitaplik[i])
  if(i >= 20 and i % 10 == 0 and i < 100):
    #print(i,len(kitaplik[i]))
    return len(kitaplik[i])
  if(i < 100):
    #print(i,hesapla(i - int(i % 10)) + hesapla(i % 10))
    return hesapla(i - int(i % 10)) + hesapla(i % 10)
  if(i % 100 == 0 and i < 1000):
    #print(i,hesapla(int(i/100)) + len(kitaplik[100]))
    return hesapla(int(i/100)) + len(kitaplik[100])
  if(i < 1000):
    #print(i,hesapla(i-(i%100)) + len(kitaplik[0]) + hesapla(i%100))
    return hesapla(i-(i%100)) + len(kitaplik[0]) + hesapla(i%100)
  if(i == 1000):
    return len(kitaplik[1000])

sonuc = 0

for i in range(1, 1001):
  sonuc += hesapla(i)

print(sonuc)