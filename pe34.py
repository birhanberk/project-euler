def faktoriyel(n):
  toplam = 1
  for a in range(1, n + 1):
    toplam *= a;
  return toplam

t = 0
for i in range(3, 50000):
  s = 0
  for j in str(i):
    s += faktoriyel(int(j))
  if(s == i):
    t += s
print(t)