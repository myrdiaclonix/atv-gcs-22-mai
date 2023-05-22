from test import test

def main():
    if test():
        a = int(input("\nInsira um número: "))
        print("Opa, vc digitou um {}".format(a))
    else:
        print("Vc n passou no teste! ROBÔ!!!")

if __name__ == "__main__":
    main()
