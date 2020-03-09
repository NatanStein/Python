arq = open("Estab_530_Antigo.txt","r")
arq_novo = open("Estab_530_Final.txt","w")
cont=1
res=[]
for linha in arq:
    if cont < 10:
        linha=linha[:216]+str(cont)+linha[217:]
    elif cont < 100:
        linha=linha[:216]+str(cont)+linha[218:]
    elif cont < 1000:
        linha=linha[:216]+str(cont)+linha[219:]
    elif cont < 10000:
        linha=linha[:216]+str(cont)+linha[220:]
    res.append(linha)
    cont+=1
for x in res:
    arq_novo.writelines(x)
arq.close()
arq_novo.close()

