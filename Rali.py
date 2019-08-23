num=int(input("Digite o número de equipes:"))
c=0
eq=[]
rf=[]
pla=[]
perg=1
while c < num:
    nm=input("\nDigite o nome da equipe: ")
    while perg <= 6:
        tempo=int(input("Digite o tempo %d em minutos: "%perg))
        while tempo < 0:
            tempo=int(input("Digite o tempo %d em minutos: "%perg))
        eq.append(tempo)
        perg=perg+1
    rf.append(nm)
    tf=eq[6*c]+eq[1+6*c]+eq[2+6*c]+eq[3+6*c]+eq[4+6*c]+eq[5+6*c]
    rf.append(tf)
    c+=1
    perg=1
vet=1
menor1=8752
menor2=8753
nome2=""
while vet < len(rf):
    if rf[vet] < menor1:
        pla.append(rf[vet-1])
        nome=rf[vet-1]
        menor2=menor1
        menor1=rf[vet]
    elif rf[vet] < menor2:
        menor2=rf[vet]
    vet=vet+2
nome2=pla[len(pla)-2]
print("A equipe campeã foi a %s com um tempo total de %d minutos"%(nome,menor1))
print("e equipe vice-campeã foi a %s com um tempo total de %d minutos"%(nome2,menor2))
print(pla)
    
        
    
