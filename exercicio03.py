peso = float(input("digite seu peso :"))
altura = float(input("digite sua altura :"))
cal = peso / (altura)**2
if cal < 18.6:
    print(f"seu IMC é {cal:.2f},você está abaixo do peso")
elif cal >= 18.6 and cal <25:
    print(f"seu IMC é {cal:.2f},você está no peso ideal")
elif cal >=25 and cal <30:
    print(f"seu IMC é {cal:.2f},você está levemente acima do peso")
elif cal >=30 and cal <35:
    print(f"seu IMC é {cal:.2f},você está com obesidade grau 1")
elif cal >= 35 and cal <40:
    print(f"seu IMC é {cal:.2f},você está com obsidade grau 2(severa")
else:
    print(f"seu IMC é {cal:.2f},obesidade grau 3 (mórbido)")

