from add import add

a = float(input("Insira um número: "))
b = float(input("Insira outro número: "))

print("Opa, vc digitou um {} e um {}".format(a, b))
print("E acontece que a soma deles é {}".format(add(a, b)))
