import csv


def ler_csv(nome_arquivo):
    """
    funcao de lê um arquivo csv e retorna uma lista de dicionario
    """
    lista = []
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for i in leitor:
            lista.append(i)
    return lista


"""vendas_itens = list[dict]
vendas = ler_csv(path_arquivo)
print(vendas)"""


def filtra_produtos_true(lista):
    """
    Filtra produtos entregue
    """
    lista_filtrada = []
    for i in lista:
        if i.get("entregue") == "true":
            lista_filtrada.append(i)
    return lista_filtrada


"""lista_prod = ler_csv(path_arquivo)
print(filtra_produtos_true(lista_prod))"""


def somar_produtos(lista_filtrada):
    """
    Soma total os produtos
    """
    valor_total = 0
    for i in lista_filtrada:
        valor_total += float(i.get("preco"))
    return valor_total
