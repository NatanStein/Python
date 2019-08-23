def resultado_aluno(n1,n2):
    if (n1+n2)/2 > 5 and n1 >= 3 and n2 >=3:
        print("Você foi aprovado!!")
    else:
        if n1 > n2:
            pf = 10-n1
            print("A nota mínima necessária para passar é tirar %.1f na provafinal"%(pf))
        else:
            pf = 10-n2
            print("A nota mínima necessária para passar é tirar %.1f na prova final"%(pf))
n1=float(input("Digite a nota da prova 1:"))
n2=float(input("Digite a nota da prova 2:"))
resultado_aluno(n1,n2)
