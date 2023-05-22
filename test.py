def test():
    """Para verificar o desempenho do usuário..."""
    a = int(input("Teste de segurança\n> Quanto é 2 + 2? "))
    b = input("> Qual a cor do céu? ")
    if a == 4 and (b == "Azul" or b == "azul"):
        return True
    return False
