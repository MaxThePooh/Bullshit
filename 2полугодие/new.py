a=[20,0,2,2,1,10]
N=len(a)
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
t=1
while t==1:
    if all(a[i]<=a[i+1] for i in range(0,N-1)):
        t=2
        print(a)
b=[20,10,5,10,20,30]
s=len(b)
bo=0
while len(b)!=2:
    bo=len(b)//2
    if b[bo]>b[bo+1]:
        b=b[bo:]
    else:
        b=b[:bo]
    print(b)
print(min(b))
