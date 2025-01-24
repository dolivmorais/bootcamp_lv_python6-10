from aula7.etl import filtra_produtos_true, ler_csv, somar_produtos

path_arquivo = "vendas.csv"

lista_f = ler_csv(path_arquivo)
lista_pf = filtra_produtos_true(lista_f)
valor_tt = somar_produtos(lista_pf)
print(valor_tt)
