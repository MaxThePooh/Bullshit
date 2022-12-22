s='012345671'
S=list(s)
S.count('1')
S.index(max(S))
print(sum(map(int,S)))
print(list(map(int,S)))
print(S[::-1])
S.sort(reverse=True)
print(S)
sp=[x for x in range(8)]
print(sp)
