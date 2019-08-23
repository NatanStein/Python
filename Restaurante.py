ing=[["Batata inglesa",250,3.50],["Queijo Minas",150,12.00],["Cenoura",100,3.00],["Carne",100,16.00]]
pratos=[["Muito Escondidinho","Batata inglesa",3,"Queijo Minas",1,"Cenoura",1],["Pastelao de Vento","Batata inglesa",4,"Carne",1]]
consumo=[["Muito Escondidinho",12],["Pastelao de Vento",1]]
cont=1
t=[]
preço=0
for x in consumo:
            for z in pratos:
                for k in ing:
                    if z[cont]==k[0]:
                        q=z[cont+1]
                        preço=preço+q*(k[1]/1000*k[2])
                    else:
                        if cont < len(z)-2:
                            cont+=2
                cont=1
                t.append(x[0])
                t.append(preço)
                print(x[0])
                print(preço)
                preço=0
print(t)
                        
                    
                
                    
