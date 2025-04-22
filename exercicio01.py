res = "s"
while res == "s":
    n1 = int(input("digite um número :"))
    if n1 % 2 == 0 and n1 <0 :
        print(f"seu número é par e negativo ")
    elif n1 % 2 == 0 and n1 > 0 :
        print(f"seu número é par e positivo ")
    elif n1 % 2 == 1 and n1 < 0 :
        print(f"seu número é ímpar e negativo ")
    elif n1 % 2 == 1 and n1 > 0 :
        print(f"seu número é ímpar e positivo ")
    res = input("deseja testar outro número ?")