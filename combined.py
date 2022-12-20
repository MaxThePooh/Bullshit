import math
def aboba():
    print("1.Сколько байт и бит займёт слово")
    print("2.Сколько символов в слове")
    print("3.Сколько байт в одном символе")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        print("Если выбрали не то введите 0")
        b=int(input("Сколько символов="))
        c=int(input("Сколько байт в одном символе=")) 
        if b<=0 or c<=0:
            print("Введи нормально")
            aboba()
        else :
            a=b*c
            print("Размер="+str(a) + "Байт")
    elif n==2:
        print("Если выбрали не то введите 0")
        a=int(input("Сколько байт="))
        c=int(input("Сколько байт в одном символе="))
        if a<=0 or c<=0:
            print("Введи нормально!")
            aboba()
        else :
            b=a/c
            print (str(b) + "символов")
    elif n==3:
        print("Если выбрали не то введите 0")
        a=int(input("Сколько байт="))
        b=int(input("Сколько символов"))
        if a<=0 or b<=0:
            print("Введи нормально")
            aboba()
        else :
            c=a/b
            print ("Байт в одном символе="+str(c) )
    else:
        print("Введи нормально!")       
def amogus():
    print("1.Размер аудиофайла")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        print("Если выбрали не то введите 0")
        D=int(input("Частота="))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра (бит)="))
        if D<=0 or T<=0 or I<=0:
            print("Введи нормально")
            amogus()
        else:
            a=D*T*I/8
            print(str(a) + "Бит")
    elif n==2:
        print("Если выбрали не то введите 0")
        A=int(input("Размер="))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра (бит)="))
        if A<=0 or T<=0 or I<=0:
            print("Введи нормально")
            amogus()
        else:
            D=8*A/(T*I)
            print ("Частота="+str(D))
    elif n==3:
        print("Если выбрали не то введите 0")
        A=int(input("Размер="))
        D=int(input("Частота="))
        I=int(input("Разрядность регистра="))
        if A<=0 or D<=0 or I<=0:
            print("Введи нормально")
            amogus()
        else:
            T=8*A/(D*I)
            print ("Время звучания="+str(T))
    elif n==4:
        print("Если выбрали не то введите 0")
        A=int(input("Размер="))
        T=int(input("Время звучания="))
        D=int(input("Частота="))
        if D<=0 or T<=0 or A<=0:
            print("Введи нормально")
            amogus()
        else:
            I=8*A/(T*I)
            print ("Разрядность регистра="+str(I))
    else:
        print("Введи нормально!")    
def abobus():
    print("1.Размер изображения")
    print("2.Глубина цвета через размер")
    print("3.Глубина цвета через количество цвето")
    print("4.Количество цветов")
    print("5.Количество пикселей")
    n=int(input("Зачем оно тебе надо (если выбрали не то введите 0):"))
    if n==1:
        print("Если выбрали не то введите 0")
        I=int(input("Глубина (бит)="))
        V=int(input("Количество пикселей="))
        if I<=0 or V<=0:
            print("Введи нормально")
            abobus()
        else :
            a=V*I
            print(str(a) + "Бит")
    elif n==3:
        print("Если выбрали не то введите 0")
        N=int(input("Количество цветов="))
        if N<=0:
            print("Введи нормально")
            abobus()
        else:
            I=math.log(N,2)
            print ("Глубина цвета="+str(I))
    elif n==3:
        print("Если выбрали не то введите 0")
        A=int(input("Размер (байт)="))
        V=int(input("Количество пикселей="))
        if A<=0 or V<=0:
            print("Введи нормально")
            abobus()
        else :
            I=A*V
            print("Глубина"+str(a/8))
    elif n==4:
        print("Если выбрали не то введите 0")
        I=int(input("Глубина цвета (бит)="))
        if I<=0:
            print("Введи нормально")
            abobus()
        else :
            N=2**I
            print ("Количество цветов="+str(N))
    elif n==5:
        print("Если выбрали не то введите 0")
        A=int(input("Размер="))
        I=int(input("Глубина="))
        if I<=0 or A<=0:
            print("Введи нормально")
            abobus()
        else :
            V=A/I
            print ("Разрядность регистра="+str(V))
    else:
        print("Введи нормально!")    
def menu1():
    print("1.Текстовые задачи")
    print("2.Звуковые задачи")
    print("3.Графические задачи")
    a=int(input("Шо тебе надо?"))
    if a==1:
        aboba()
    elif a==2:
        amogus()
    elif a==3:
        abobus()
    else:
        print("Введи нормально!")
def morza():
    s=input("Введи слово разбитое на пробелы ЗАГЛАВНЫМИ латинскими буквами: ")
    str_list=s.split(sep=' ')
    d=dict(A='.-', B='-...',W='.--',G='--.',D='-..',E='',V='',Z='',I='',J='',K='',L='',M='',N='',O='---',P='.--.',R='.-.',S='...',T='',U='..--',F='..-.',H='....',C='-.-.',Q='---.-',X='-..-')
    i=len(str_list)
    for k in range(i):
        print(d[str_list[k]], end=" ")
        str_c=d[str_list[k]].split()
def distance(x,y):
    k=7
    for i in range(0,7):
        if x%10==y%10:
            k=k-1
            x=x//10
            y=y//10
    return k
def hem():
    chisla='0123456789'
    chisla_spicok=list(chisla)
    print(chisla_spicok)
    haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    haming_spisok=haming.split()
    print(haming_spisok)
    cod=int(input("код= "))
    min=distance(cod,int(haming_spisok[0]))
    imin=0
    for i in range(0,9):
        D=distance(cod,int(haming_spisok[i]))
        if D<min:
            min=D
            imin=i
    print(min)
    if min==0:
        print(f"код верный: символ {chisla_spicok[imin]}")
    elif min==1:
        print(f"код исправлен: символ {chisla_spicok[imin]}")
    else:
        print("код неверный")
def tabl():
    p=int(input("основание (2<p<10)"))
    n=0
    for x in range(1,p):
        for y in range(1,p):
            n=((x*y)//p)*10+x*y%p
            print(n,end=" ")
        print(" ")
def ndc():
    p=int(input("Число: "))
    n=int(input("В какой системе: "))
    k=1
    d=0
    while(n!=0):
        d+=n%10*k
        k=k*p
        n=n/10
    print(d)
def cdn():
    n = int(input("Какое число: "))
    c=int(input("В какую систему:"))
    b = ''
    while n > 0:
        b = str(n % c) + b
        n = n // c
    print(b)
def men0():
    print(" ")
    print("1.Морза")
    print("2.Хемминг")
    print("3.Решатель")
    print("4.Перевод из n-ой в 10-ую")
    print("5.таблица умножения n-ой")
    print("6.Из десятичной в n-ую")
    m=int(input("Выберите (если выбрали не то введите 0):"))
    if(m==1):
        morza()
    elif(m==2):
        hem()
    elif(m==3):
        menu1()
    elif(m==4):
        ndc()
    elif(m==5):
        tabl()
    elif(m==6):
        cdn()
    else:
        print("Ошибка ввода!")
while 1 >0:
    men0()
