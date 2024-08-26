import numpy as np
import pandas as pd

def preencher_dias_faltantes(df:pd.DataFrame, multi_indice:list|str, corpo_dataset:str, limite_dias:int) -> pd.DataFrame:
    dataframe_agrupado = df.groupby(multi_indice[0])
    
    novo_dataframe = pd.DataFrame(
        index = pd.MultiIndex.from_product(
            [dataframe_agrupado.groups.keys(), range(1, limite_dias)],
            names = multi_indice
        ),
        columns = [corpo_dataset]
    )
    novo_dataframe.update(df.set_index(multi_indice))
    
    return novo_dataframe

def pivotear_dataset_ureia(df_ureia:pd.DataFrame, coluna_indice:str, coluna_pivoteada:str, coluna_para_novos_valores:str) -> pd.DataFrame:
    df_pivoteado = df_ureia.pivot(
        index = coluna_indice,
        columns = coluna_pivoteada,
        values = coluna_para_novos_valores
    )
    df_pivoteado.columns = ["ureia_dia_" + str(coluna) for coluna in df_pivoteado.columns]

    return df_pivoteado

def pivotear_dataset_creatinina(df_creatinina:pd.DataFrame, coluna_indice:str, coluna_pivoteada:str, coluna_para_novos_valores:str) -> pd.DataFrame:
    df_pivoteado = df_creatinina.pivot(
        index = coluna_indice,
        columns = coluna_pivoteada,
        values = coluna_para_novos_valores
    )
    df_pivoteado.columns = ["creatinina_dia_" + str(coluna) for coluna in df_pivoteado.columns]

    return df_pivoteado
