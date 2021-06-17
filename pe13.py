with open("deneme.txt","r") as dosya:
    liste = dosya.readlines()
    toplam=0
    dizi=[]
    for i in range(0,100):
        toplam+=int(liste[i])
    for k in str(toplam):
        if(len(dizi)<10):
            dizi.append(int(k))
    print(dizi)
