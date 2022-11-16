def aboba():
    print("1.Сколько байт и бит займёт слово")
    print("2.Сколько символов в слове")
    print("3.Сколько байт в одном символе")
    n=int(input("Выберите:"))
    if n==1:
        b=int(input("Сколько символов="))
        c=int(input("Сколько байт в одном символе="))
        a=b*c
        print(str(a) + "Байт")
        print(str(a*8) + "Бит")
    elif n==2:
        a=int(input("Сколько байт="))
        c=int(input("Сколько байт в одном символе="))
        b=a/c
        print (str(b) + "символов")
    elif n==3:
        a=int(input("Сколько байт"))
        b=int(input("Сколько символов"))
        c=a/b
        print (str(c) + "Байт в одном символе")
    else:
        print("Неверный ввод!")    
    
def amogus():
    print("1.Размер аудиофайла")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра")
    n=int(input("Выберите:"))
    if n==1:
        D=int(input("Частота"))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра"))
        a=D*T*I/8
        print(str(a) + "Байт")
        print(str(a*8) + "Бит")
    elif n==2:
        A=int(input("Размер"))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра"))
        D=8*A/(T*I)
        print (str(D) + "Частота")
    elif n==3:
        A=int(input("Размер"))
        T=int(input("Частота="))
        I=int(input("Разрядность регистра"))
        T=8*A/(D*I)
        print (str(T) + "Время звучания")
    elif n==4:
        A=int(input("Размер"))
        T=int(input("Время звучания="))
        D=int(input("Частота"))
        I=8*A/(T*I)
        print (str(I) + "Разрядность регистра")
    else:
        print("Неверный ввод!")    

def abobus():
    print("1.Размер ")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра")
    if n==1:
        D=int(input("Частота"))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра"))
        a=D*T*I/8
        print(str(a) + "Байт")
        print(str(a*8) + "Бит")
    elif n==2:
        A=int(input("Размер"))
        T=int(input("Время звучания="))
        I=int(input("Разрядность регистра"))
        D=8*A/(T*I)
        print (str(D) + "Частота")
    elif n==3:
        A=int(input("Размер"))
        T=int(input("Частота="))
        I=int(input("Разрядность регистра"))
        T=8*A/(D*I)
        print (str(T) + "Время звучания")
    elif n==4:
        A=int(input("Размер"))
        T=int(input("Время звучания="))
        D=int(input("Частота"))
        I=8*A/(T*I)
        print (str(I) + "Разрядность регистра")
    else:
        print("Неверный ввод!")    

def menu1():
    print("1.Текстовые задачи")
    print("2.Звуковые")
    print("3.")
    a=int(input("Выберите тип задачи?"))
    if a==1:
        aboba()
    elif a==2:
        amogus()
    elif a==3:
        abobus()
    else:
        print("Введи нормально!")
while 1 >0:
    menu1()
