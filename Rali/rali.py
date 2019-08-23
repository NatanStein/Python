def converte (t):
    h=t//3600
    min=t%3600//60
    sec=t%3600%60
    if h < 10:
        h="0"+str(h)
    if sec < 10:
        sec="0"+str(sec)
    if min < 10:
        min="0"+str(min)
    return str(h)+":"+str(min)+":"+str(sec)
def le_arq_equipes():
    arq_equipes=open("equipes.txt","r")
    texto=arq_equipes.read()
    texto=texto.strip()
    texto=texto.split("\n")
    contador=0
    corredores=[]
    while contador < len(texto):
        corredores.append([texto[contador],texto[contador+1]])
        contador+=2
    arq_equipes.close()
    return corredores
def le_arq_tempos ():
    arq_tempos=open("tempos.txt","r")
    for linha in arq_tempos:
        linha=linha.strip()
        linha=linha.split(",")
        if linha[0] != 6 :
            cont=6-int(linha.pop(0))
            while cont > 0:
                linha.append(9999)
                cont-=1
        else:
            linha.pop(0)
        for i,x in enumerate (corredores):
            if linha[0] == x[1]:
                linha.pop(0)
                corredores[i]=[x[0],x[1],linha]
    arq_tempos.close()
    return corredores
cont=0
maior=9999
ano=2019
corredores=le_arq_equipes()
corredores=le_arq_tempos()
while cont < 6:
    for i,x in enumerate (corredores):
        if int(x[2][cont]) < maior:
            maior=int(x[2][cont])
            indice=i
        elif int(x[2][cont]) == maior:
            if int(x[0]) < ano:
                maior=int(x[2][cont])
                indice=i
    if len(corredores[indice][1]) <= 4:
        esp="\t\t\t"
    else:
        esp="\t\t"
    for x in corredores[indice][2]:
        corredores[indice][2].append(int(corredores[indice][2].pop(0)))
    tempototal=converte(sum(corredores[indice][2]))
    print("Equipe campeã no trecho %d: %s%sAno de criação: %s"%(cont+1,corredores[indice][1],esp,corredores[indice][0]))
    print("Tempo no trecho atual: %s\t\t\tTempo total da equipe: %s"%(maior,tempototal))
    cont+=1
    indice=0
    maior=9999
    ano=2019


            
