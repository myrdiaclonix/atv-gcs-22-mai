from add import add
from test import test

def main():
    if test():
        a = float(input("\nInsira um número: "))
        b = float(input("Insira outro número: "))

        print("Opa, vc digitou um {} e um {}".format(a, b))
        print("E acontece que a soma deles é {}".format(add(a, b)))
    else:
        print("Vc n passou no teste! ROBÔ!!!")

if __name__ == "__main__":
    main()
