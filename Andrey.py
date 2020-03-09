import random
cont=0
res=[
['a', 'n'],
['b', 'i'],
['c', 'e'],
['d', 'h'],
['e', 'd'],
['f', 'r'],
['g', 'v'],
['h', 'i'],
['i', 'o'],
['j', 'q'],
['k', 't'],
['l', 'l'],
['m', 'r'],
['n', 'q'],
['o', 'g'],
['p', 'l'],
['r', 's'],
['q', 'k'],
['s', 'y'],
['t', 'c'],
['u', 'r'],
['v', 'e'],
['w', 'h'],
['x', 'h'],
['y', 'u'],
['z', 'p']]
s = input("Digite a sua palavra: ")
t=s.splash()
print(t)
sr = ""
for x in s:
    for i in res:
        if x == i[0]:
            sr=sr+i[1]
            break
print(sr)
            

