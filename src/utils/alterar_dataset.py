import numpy as np
import pandas as pd


def preencher_dias_faltantes(df:pd.DataFrame, multi_indice:list[str]|str, corpo_dataset:str, limite_dias:int) -> pd.DataFrame:
    if isinstance(multi_indice, list):
        dataframe_agrupado:pd.DataFrame = df.groupby(multi_indice[0])
    else:
        dataframe_agrupado:pd.DataFrame = df.groupby(multi_indice)
    
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

def __verificar_valor_em_linha(serie:pd.Series, valor:int|float) -> pd.Series:
    for indice, _ in serie.items():
        if serie[indice] == valor:
            serie[indice] = np.nan
    
    return serie

def deletar_valores_absurdos(df:pd.DataFrame, valor:int|float) -> pd.DataFrame:
    for coluna in df.columns:
        df[coluna] = __verificar_valor_em_linha(df[coluna], valor)
        
    return df

def preencher_valores_faltantes_linha(df:pd.DataFrame) -> pd.DataFrame:
    df_transposto = df.T
    
    for coluna in df_transposto.columns:
        df_transposto[coluna] = df_transposto[coluna].fillna(
            df_transposto[coluna].shift(
                fill_value = df_transposto[coluna].iloc[0]
            )
        )

    return df_transposto.T

def concatenar_dois_datasets_por_paciente(df_esquerda:pd.DataFrame, df_direita:pd.DataFrame) -> pd.DataFrame:
    cols_to_use = df_direita.columns.difference(df_esquerda.columns)
    
    return pd.merge(df_esquerda,
                    df_direita[cols_to_use],
                    left_index = True,
                    right_index = True,
                    how = "outer")
