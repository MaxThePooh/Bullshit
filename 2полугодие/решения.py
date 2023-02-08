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
                
#print(f23(1,10,10)*f23(10,35,25))

