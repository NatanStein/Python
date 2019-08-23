def menorDigito (n):
    print(n)
    if n < 10:
        return int(n)
    else:
        a=(n%100-n%10)/10
        b=n%10
        if a < b :
            return menorDigito((n//100)*10+a)
        else:
            return menorDigito(n//100*10+b)

print(menorDigito(12345))
