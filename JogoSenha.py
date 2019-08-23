import random
def resposta ():
    resp=input("Você gostaria de jogar novamente(S/N)? ")
    while resp != "S" and resp != "N":
        resp=input("Não entendi a sua resposta..\n\t\tVocê gostaria de jogar denovo(S/N)? ")
    return resp

    
def jogoSenha(senha):
    t=1
    while t<6:
        n=int(input("Digite a senha:"))
        if n < 1 or n > 50:
            n=int(input("Digite a senha no intervalo [1,50]:"))
            while n < 1 or n > 50:
                n=int(input("Digite a senha no intervalo [1,50]:"))
        if senha==n:
            print("Parabens!!,você acertou a senha (%d)"%senha)
            resp=resposta()
        elif senha == n+1 or senha==n-1:
            print("TA QUENTE!!\n")
        else:
            if n < senha:
                print("A senha é maior\n")
            elif n > senha:
                print("A senha é menor\n")
        t=t+1
        if t==6:
            print("Você perdeu a senha era %d"%senha)
            resp=resposta()
    return resp
#
#Bloco Principal
#
dnv="S"
while dnv=='S':
    senha=random.randint(1,50)
    dnv=jogoSenha(senha)
print("Obrigado pelo jogo")
        
             


