def f5():
  for N in range(516):
    b=f'{N:b}'
    if N%2==0:
        b+='10'
    else:
        b='1'+b+'01'
    if int(b,2)>516:
        print(N)
        break
        
        
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2

            if a==y: count+=1
    return count
                
def f23(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) +f(x*2,y)
#print(f(1,10)*f(10,35))
#print(f23(1,10,10)*f23(10,35,25))

count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                        count+=1
print(count)

from itertools import product
nums=product('01234567',repeat=5)
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('6')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)

