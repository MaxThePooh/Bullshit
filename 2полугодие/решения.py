def f2()
print('x y z w')
  for x in range(2):
    for y in range(2):
        for z in range(2):
           for w in range(2):
              if (not(y<=x) or (z<=w) or not(z))==False:
                 print(x, y, z, w)

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
        
def f24()
  with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S').replace('A','G').replace('O','G')
    s=s.replace('SG','1')
    count=0
    m=0
    for i in s:
        if i=='1':
            count+=1
        else:
            if count>m:
                m=count
            count=0
    print(m)
    with open('24.txt') as f:
        s=f.readline().replace('AB','1').replace('AC','1').replace('A',' ').replace('B',' ').replace('C',' ')
        print(max(len(x) for x in s.split()))

    
def f26()
  with open('26.txt') as f:
    s=[int(x) for x in f]
    s.pop(0)
    s.sort(reverse=True)
    count=1
    m=s[0]

    for i in range(1,len(s)):
        if s[i]+3<=m:
            m=s[i]
            count+=1
print(count,m)

    
def f25()
  count=0
for i in range(2023,10**10,2023):
    ist=str(i)
    if ist[0]=='1' and ist[2:6]=='2139' and i%10==4:
        print(i,i//2023)
   def f25():
    for a in range(10):
        for b in range(10):
            x=int(f'12345{a}6{b}8')
            if x%17==0:
                print(x,x//17)

        
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

def f17():
   with open('17.txt') as f:
    nums=[int(x) for x in f]
    c=list(map(abs,nums))
    a=[]
    for i in range(len(c)-1):
        if c[i]%10==3:
            a.append(c[i])
    m=max(a)
    count=0
    summ=[]
    #for i in range(len(nums)-1):
       #if((nums[i]%10==3 and nums[i+1]%10!=3) or (nums[i]%10!=3 and nums[i+1]%10==3)):
    for i in range(len(c)-1):
        if((c[i]%10==3 and c[i+1]%10!=3) or (c[i]%10!=3 and c[i+1]%10==3)):
            if nums[i]**2+nums[i+1]**2>=m**2:
                count+=1
                summ.append(nums[i]**2+nums[i+1]**2)
    print(count)
    print(max(summ))
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

def f16()
    import sys
  sys.setrecursionlimit(3000)
  def f(n):
      if n==1:
          return 1
      else:
          return n*f(n-1)
  print(f(2023)/f(2020))



  itog1=itog2=1
  for x1 in range(1,2024):
      itog1=itog1*x1
  for x2 in range(1,2021):
      itog2=itog2*x2
  print(itog1/itog2)

  
  
  def f27():  
    from math import ceil

    f = open("27_B.txt")
    n = int(f.readline())
    elems = []
    sum = 0
    rightSum = 0
    leftSum = 0
    for i in range(0, n):
        a, b = map(int, f.readline().split())
        elems.append([a, ceil(b / 36)])
    cost = [0] * n
    for i in range(1, n):
        cost[0] += (elems[i][0] - elems[0][0]) * elems[i][1]
        rightSum += elems[i][1]
    for i in range(1, n):
        leftSum += elems[i - 1][1]
        cost[i] = cost[i - 1] - rightSum * (elems[i][0] - elems[i - 1][0]) + leftSum * (elems[i][0] - elems[i - 1][0])
        rightSum -= elems[i][1]
    print(min(cost))
    
    with open ('27_B.txt') as f:
    n=[x for x in f] # записываем строки
    n.pop(0) #убираме первую строку
    sp=[]
    k=[]
    ind=[]
    for i in n:
        sp.append(list(map(int,i.split()))) # переводим значения в списке в числа
    for i in range(len(sp)):
        k.append((sp[i][1]-1)//36+1) # находим кол-во контейнеров
    for i in range(len(sp)):
        ind.append(sp[i][0])#сохраняем километраж пунктов 
    sp=list(zip(ind,k))#соединяем километраж и кол-во контейнеров
    costs=[]
    for i in range(549715,549735,1):# в этом цикле мы выводим значения приближаясь к минимальному
        pos=sp[i][0]
        cost=0
        for x in sp:
            cost=cost+abs(pos-x[0])*x[1]#вычисляем стоимость в этот пункт
        costs.append(cost)
        print(i,sp[i][0],cost)
  
  
