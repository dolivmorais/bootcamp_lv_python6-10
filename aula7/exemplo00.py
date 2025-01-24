"""def imprimir(texto, n):
    for i in range(n):
        print(texto)

    print(texto)

imprimir("Olá", 10)"""


# tabulada
def tabuada(p1: int, p2: int) -> int:
    """
    Monta uma tabuada
    """
    for i in range(p1, p2):
        for j in range(p1, p2):
            v = i * j
            print(f"{i} x {j} = {v} ")


tabuada(1, 10)
