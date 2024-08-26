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
