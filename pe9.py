for i in range(200,500):
  for j in range(200,500):
    if(i>=j):
      continue
    for k in range(200,500):
      if(j>=k):
        continue
      if(i**2+j**2==k**2):
        if(i+j+k==1000):
          print("Bulduk!!!!!!!----->>",i,j,k)
          print(i*j*k)