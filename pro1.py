s=int(input())
b=[]
for i in range(s):
  c=input()
  b.append(c)
d=[]
for i in zip(*b):
  if(i.count(i[0])==len(i)):
    d.append(i[0])
  else:
    break
print(''.join(d))
