n,t=input().strip().split(" ")
t=int(t)
i=0;
while i<len(n)-1 and t:
	if(n[i]>n[i+1]):
		k-=1
		n=n[:i]+n[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
re=n[:len(n)-t]
print(re)
