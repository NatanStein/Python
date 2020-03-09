cont=1
soma=0
while cont <=10:
    if cont%2==0:
        soma-=1/cont
    else:
        soma+=1/cont
    print(soma)
    cont+=1
print(soma)
    
