import math
def convertjuliano (dia,mes,ano):
    if mes < 3:
        ano=ano-1
        mes=mes+12
    A=ano//100
    B=A//4
    C=2-A+B
    D=int(365.25*(ano+4716))
    E=int(30.6001*(mes+1))
    return D+E+dia+0.5+C-1524.5
def separadata(data):
    dia=data[0:2]
    mes=data[3:5]
    ano=data[6:]
    t=[int(dia),int(mes),int(ano)]
    return t
def CalculaCiclo(difnascimento,dc):
    return math.sin(2*math.pi*(difnascimento)/dc)
def MostraCicloMensagem(x,cddisc,CF,CE,CINTELEC,CINT):
    print("Na prova do dia %s da materia %s o seu biorritimo será:\nCiclo fisico = %d"%(x,cddisc,CF)+"%")
    if CF <= 0:
        print("Cuidado!!")
    print("Ciclo emocional = %d"%CE+"%")
    if CE <= 0:
        print("Cuidado!!")
    print("Ciclo intelectual = %d"%CINTELEC+"%")
    if CINTELEC <= 0:
        print("Cuidado!!")
    print("Ciclo intuitivo = %d"%CINT+"%")
    if CINT <= 0:
        print("Cuidado!!")
def biorritmo(datanasc,table):
    dtn=separadata(datanasc)
    dtnj=convertjuliano(dtn[0],dtn[1],dtn[2])
    for el in table:
        cddisc=el[0]
        for x in el[1:]:
            dtp=separadata(x)
            dtpj=convertjuliano(dtp[0],dtp[1],dtp[2])
            CF=int(CalculaCiclo(dtpj-dtnj,23)*100)
            CE=int(CalculaCiclo(dtpj-dtnj,28)*100)
            CINTELEC=int(CalculaCiclo(dtpj-dtnj,33)*100)
            CINT=int(CalculaCiclo(dtpj-dtnj,38)*100)
            MostraCicloMensagem(x,cddisc,CF,CE,CINTELEC,CINT)
    return 
#
# Bloco Principal
#

cont=1
DisciplinaeProvas=[]
datanascimento=input("Digite a sua data de nascimento no formato dd/mm/aaaa:")
while True:
    sairtotal=input("Se ja digitou todas as provras e o codigo da disciplina digite Exit,\nSe não aperte enter: ")
    if sairtotal=="Exit":
        print("")
        break
    numdisc=input("Digite o codigo da disciplina: ")
    aux=[numdisc]
    while True:
        sair=input("Se ja digitou todas as provras digite Exit,\nSe não aperte enter: ")
        if sair == "Exit":
            break
        dtp=input("Digite a data da prova %d no formato dd/mm/aaaa: "%cont)
        aux.append(dtp)
        cont+=1
    DisciplinaeProvas.append(aux)
    aux=[]
    cont=1
biorritmo(datanascimento,DisciplinaeProvas)
    
    
