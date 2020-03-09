import random
t="0010010010"
escolha = random.choices(t)
print(escolha[0])
if escolha[0] == "1":
    print("Desviar")
else:
    print("Não desviar")
