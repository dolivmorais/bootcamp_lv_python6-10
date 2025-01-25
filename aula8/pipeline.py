from etl import pipeline_calculo_cocolidade_kpi_venda

pasta_agrupamento = "data"
format_saida = ["csv", "parquet"]


pipeline_calculo_cocolidade_kpi_venda(pasta_agrupamento, format_saida)
