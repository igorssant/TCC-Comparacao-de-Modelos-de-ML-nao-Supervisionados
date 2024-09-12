import numpy as np
import pandas as pd

def preencher_dias_faltantes(df:pd.DataFrame, multi_indice:list|str, corpo_dataset:str, limite_dias:int) -> pd.DataFrame:
    dataframe_agrupado:pd.DataFrame = df.groupby(multi_indice[0])
    
    novo_dataframe:pd.DataFrame = pd.DataFrame(
        index = pd.MultiIndex.from_product(
            [dataframe_agrupado.groups.keys(), range(1, limite_dias)],
            names = multi_indice
        ),
        columns = [corpo_dataset]
    )
    novo_dataframe.update(df.set_index(multi_indice))
    
    return novo_dataframe

def pivotear_dataset_ureia(df_ureia:pd.DataFrame, coluna_indice:str, coluna_pivoteada:str, coluna_para_novos_valores:str) -> pd.DataFrame:
    df_pivoteado:pd.DataFrame = df_ureia.pivot(index = coluna_indice,
                                               columns = coluna_pivoteada,
                                               values = coluna_para_novos_valores)
    df_pivoteado.columns = ["ureia_dia_" + str(coluna) for coluna in df_pivoteado.columns]

    return df_pivoteado

def pivotear_dataset_creatinina(df_creatinina:pd.DataFrame, coluna_indice:str, coluna_pivoteada:str, coluna_para_novos_valores:str) -> pd.DataFrame:
    df_pivoteado:pd.DataFrame = df_creatinina.pivot(index = coluna_indice,
                                                    columns = coluna_pivoteada,
                                                    values = coluna_para_novos_valores)
    df_pivoteado.columns = ["creatinina_dia_" + str(coluna) for coluna in df_pivoteado.columns]

    return df_pivoteado

def despivotear_dataset(df:pd.DataFrame,
                        coluna_id:str|list[str],
                        colunas_colapsar:list[str]|str,
                        nome_coluna_colapsada:str,
                        nome_coluna_de_valores:str) -> pd.DataFrame:
    df_despivoteado:pd.DataFrame = df.melt(id_vars = coluna_id,
                                           value_vars = colunas_colapsar,
                                           value_name = nome_coluna_colapsada,
                                           var_name = nome_coluna_de_valores)
    return df_despivoteado

def multi_indexar_dataset(df:pd.DataFrame, indices:str|list[str]) -> pd.DataFrame:
    df_multi_indexado:pd.DataFrame = df.set_index(keys = ["subject_id", "day"])
    return df_multi_indexado.sort_index()
