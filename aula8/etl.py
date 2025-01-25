import glob
import os

import pandas as pd


# consolidação dos arquiovos json
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_lista = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_lista, ignore_index=True)
    return df_total


# função de transformação
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["total"] = df["quantidade"] * df["venda"]
    return df


# carregar dados
def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet")


def pipeline_calculo_cocolidade_kpi_venda(pasta, formato_saida):
    df = extrair_dados_e_consolidar(pasta)
    df_calculido = calcular_kpi_total_vendas(df)
    carregar_dados(df, formato_saida)
