try:
    a = float(input("Введите первое число: "))
    znakprov = "+-/*"

    while True:

        znak = input("Введите знак операции (+, -, /, *): ")


        if znak in znakprov:
            break
        elif "" in znak:
            print("Введите один из знаков: +, -, /, *")


    b = float(input("Введите второе число: "))

    if "+" in znak:
        plus = a + b
        if plus % 1 != 0:
            fplus = float(plus)
            print(fplus)
        else:
            iplus = int(plus)
            print(iplus)

    elif "-" in znak:
        minus = a - b
        if minus % 1 != 0:
            fminus = float(minus)
            print(fminus)
        else:
            iminus = int(minus)
            print(iminus)

    elif "/" in znak:
        delenie = a / b
        if delenie % 1 != 0:
            fdelenie = float(delenie)
            print(fdelenie)
        else:
            idelenie = int(delenie)
            print(idelenie)

    elif "*" in znak:
        umnog = a * b
        if umnog % 1 != 0:
            fumnog = float(umnog)
            print(fumnog)
        else:
            iumnog = int(umnog)
            print(iumnog)

except ValueError:
    print("Некорректный ввод, можно вводить только цифры")
except ZeroDivisionError:
    print("На 0 делить нельзя")
except Exception:
    print("dsggd")