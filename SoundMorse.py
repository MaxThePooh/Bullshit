import winsound
s=input()
str_list=s.split(sep=' ')
print(str_list)
d=dict(A='.-', B='-...',W='.--',G='--.',D='-..',E='',V='',Z='',I='',J='',K='',L='',M='',N='',O='---',P='.--.',R='.-.',S='...',T='',U='..--',F='..-.',H='....',C='-.-.',Q='---.-',X='-..-')
i=len(s)
for k in range(i):
    print(d[str_list[k]])
    str_c=d[str_list[k]].split()
    g=len(d[str_list[k]])
    for l in range(g):
        if(str_c[l-1]=='.'):
            winsound.Beep(100,550)
        else:
            winsound.Beep(1000,1050)
