def learqjogadores(nome):
    arq_jog=open(nome,"r")
    t=[]
    for linha in arq_jog:
        linha=linha.strip()
        t.append([0,0,linha])
    arq_jog.close()
    return t
def busca (lista,nome):
    for i,x in enumerate (lista):
        if x[2]==nome:
            return i
    return -1
def processa_resultado(t,nome):
    arq_part=open(nome,"r")
    for linha in arq_part:
        linha=linha.strip()
        l=linha.split(",")
        nome1=l[0]
        set1=int(l[1])
        nome2=l[2]
        set2=int(l[3])
        in1=busca(jogadores,nome1)
        in2=busca(jogadores,nome2)
        if in1!= -1 and in2 != -1:
            t[in1][0]=t[in1][0]+set1
            t[in2][0]=t[in2][0]+set2
            if set1 > set2:
                t[in1][1]=t[in1][1]+1
            else:
                t[in2][1]=t[in2][1]+1
    arq_part.close()
    return t     
jogadores=learqjogadores("jogadores.txt")
listafinal=processa_resultado(jogadores,"resultados.txt")
ganhador=""
maior=0
for i,x in enumerate (jogadores):
    if x[1] > maior:
        nome=x[2]
        maior=x[1]
        sets=x[0]
    elif x[1]==maior:
        i1=busca(jogadores,nome)
        nome2=jogadores[i][2]
        if jogadores[i][0] > jogadores[i1][0]:
            nome=nome2
            maior=jogadores[i][1]
            sets=jogadores[i][0]
print("O ganhador com %d vitorias e %d sets vencidos foi %s"%(maior,sets,nome))

