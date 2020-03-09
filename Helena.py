import math 
def taxaOver50Ex1(peso):
    if peso > 50:
        return math.ceil((peso-50))*4
    return 0
def calcPrecoEx2(tamanho):
    return (math.ceil((tamanho/3)/18))*80
def calcTempoEx3(tamanho,vel):
    mb = tamanho*8
    sec = mb/vel
    minutos = sec//60
    return str(int(minutos))+":"+str(int(sec%60))
def leetEx4(palavra):
    palavra=palavra.lower()
    palavra=palavra.replace("o","0")
    palavra=palavra.replace("i","1")
    palavra=palavra.replace("e","3")
    palavra=palavra.replace("a","4")
    palavra=palavra.replace("s","5")
    palavra=palavra.replace("t","7")
    return palavra
def verifVogalEx5 (letra):
    letra=letra.lower()
    return letra in "aeiou"
def compraCarneEx6 (listaC):
    Lretorno=[]
    for i,x in enumerate (listaC):
        if x != 0 and i != 3:
            Lretorno.append(x)
            if i == 0:
                if x > 5:
                    Lretorno.append(x*5.80)
                else:
                    Lretorno.append(x*4.90)
            elif i == 1:
                if x > 5:
                    Lretorno.append(x*6.80)
                else:
                    Lretorno.append(x*5.90)
            else:
                if x > 5:
                    Lretorno.append(x*7.80)
                else:
                    Lretorno.append(x*6.90)
        if i == 3:
            Lretorno.append(x)
            if x:
                Lretorno.append(Lretorno[1]-Lretorno[1]*95/100)
                Lretorno.append(Lretorno[1]*95/100)
            else:
                Lretorno.append(0)
                Lretorno.append(Lretorno[1])
    return Lretorno
def CalcMcustoEx7 (tamanho):
    Lretorno=[]
    Nlitros = tamanho/6
    Lretorno.append(Nlitros//18)
    Lretorno.append(math.ceil((Nlitros%18)/3.6))
    Lretorno.append(math.ceil((Nlitros%18)/3.6)-((Nlitros%18)/3.6))
    Lretorno.append(Lretorno[0]*80+Lretorno[1]*25)
    return Lretorno
def coulombEx8(q1,q2,d):
    return ((8.98*(10**9))*q1*q2)/(d*d)
#
# Bloco Principal 
#
print(taxaOver50Ex1(72.5))
print(calcPrecoEx2(623))
print(calcTempoEx3(1526,15))
print(leetEx4("saltador"))
print(verifVogalEx5("f"))
A=[0,8,0,False]
print(compraCarneEx6(A))
print(CalcMcustoEx7(623))
print(coulombEx8(1*10**(-6),2*10**(-3),0.5))
