x=2
sayac=1
enbuyuk=1
hafiza=0
for i in range(x,1000000):
    hafiza=i
    while True:
        if(i==1):
            break
        elif(i%2==0):
            i=int(i/2)
            sayac+=1
        elif(i%2==1):
            i=int((i*3)+1)
            sayac+=1
    if(enbuyuk<sayac):
        enbuyuk=sayac
        print("sayac",sayac+1)
        print(hafiza)
    sayac=0
