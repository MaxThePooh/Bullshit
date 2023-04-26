from itertools import product
msk=[0,712,673,1075,875,1622,423]
spb=[712,0,1385,1800,1577,2348,1128]
chb=[673,1385,0,1499,239,2046,244]
rnd=[1075,1800,1499,0,1287,551,1266]
usk=[875,1577,239,1287,0,1835,442]
sch=[1622,2348,2046,551,1835,0,1813]
nnd=[423,1128,244,1266,442,1813,0]
tabl=[msk,spb,chb,rnd,usk,sch,nnd]
alf='0123456'
a=product(alf,repeat=7)
maxi=0
for i in a:
    if all(i.count(x)==1 for x in alf):
        s=0
        for l in range(len(i)-1):
            s+=tabl[int(i[l])][int(i[l+1])]
            if s >=maxi:
                maxi=s
print(maxi)
