def CalcPos (pos,t):
    for i,x in enumerate (t):
        for j,y in enumerate (x):
            if pos == y:
                t[i][j]="CA"
                if i >=2 and j < 7:
                    t[i-2][j+1]="OO"
                if i >=2 and j > 0:
                    t[i-2][j-1]="OO"
                if i < 6 and j < 7:
                    t[i+2][j+1]="OO"
                if i < 6 and j > 0:
                    t[i+2][j-1]="OO"
                if i > 0 and j > 1:
                    t[i-1][j-2]="OO"
                if i > 0 and j < 6:
                    t[i-1][j+2]="OO"
                if i < 7 and j < 6:
                    t[i+1][j+2]="OO"
                if i < 7 and j > 2:
                    t[i+1][j-2]="OO"
                return t
    print("Posição invalida")
    return t
    
alf="ABCDEFGH"
num="12345678"
t=[[],[],[],[],[],[],[],[]]
cont=0
s=""
for x in alf:
    for y in num:
        t[cont].append(x+y)
        s=s+x+y+" "
    s=s+"\n"
    cont+=1
print(s+"\n")
pos=str(input("Digite a posição: "))
t=CalcPos(pos,t)
s=""
for x in t:
    for y in x:
        s=s+y+" "
    s=s+"\n"
print("\n"+s)       
