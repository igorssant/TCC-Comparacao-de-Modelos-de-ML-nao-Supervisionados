import sys
sys.path.append("./utils/")
import pandas as pd

def __realizar_contagem_ureia(paciente:pd.Series, valor_maximo_aceitavel:float) -> float:
    quantidade_dias:int = 0
    
    for valor_ureia in paciente:
        if valor_ureia > valor_maximo_aceitavel:
            quantidade_dias = 1 + quantidade_dias
    
    return quantidade_dias

def __contagem_dias_ureia_alta(paciente:pd.Series, sexo:int) -> int:
    quantidade_dias:int = 0
    valor_maximo_aceitavel:list[float] = [40.0, # pacientes do sexo feminino
                                          50.0] # pacientes do sexo masculino
    
    # paciente do sexo feminino
    if sexo == 1:
        quantidade_dias = __realizar_contagem_ureia(paciente, valor_maximo_aceitavel[0])
    # paciente do sexo masculino
    else:
        quantidade_dias = __realizar_contagem_ureia(paciente, valor_maximo_aceitavel[1])
    
    return quantidade_dias

def contagem_dias_ureia_alta(df:pd.DataFrame) -> list[float]:
    lista_quantidade_dias:list[float] = []
    lista_sexo:list[int] = df["gender"].to_list()
    df = df.drop(columns = ["gender"], inplace = False)
    
    for paciente, sexo in zip(df.index, lista_sexo):
        lista_quantidade_dias.append(__contagem_dias_ureia_alta(df.loc[paciente], sexo))
    
    return lista_quantidade_dias

def __realizar_contagem_creatinina(paciente:pd.Series, valor_maximo_aceitavel:float) -> float:
    quantidade_dias:int = 0
    
    for valor_creatinina in paciente:
        if valor_creatinina > valor_maximo_aceitavel:
            quantidade_dias = 1 + quantidade_dias
    
    return quantidade_dias

def __contagem_dias_creatinina_alta(paciente:pd.Series, sexo:int) -> int:
    quantidade_dias:int = 0
    valor_maximo_aceitavel:list[float] = [1.1, # pacientes do sexo feminino
                                          1.3] # pacientes do sexo masculino
    
    # paciente do sexo feminino
    if sexo == 1:
        quantidade_dias = __realizar_contagem_creatinina(paciente, valor_maximo_aceitavel[0])
    # paciente do sexo masculino
    else:
        quantidade_dias = __realizar_contagem_creatinina(paciente, valor_maximo_aceitavel[1])
    
    return quantidade_dias

def contagem_dias_creatinina_alta(df:pd.DataFrame) -> list[float]:
    lista_quantidade_dias:list[float] = []
    lista_sexo:list[int] = df["gender"].to_list()
    df = df.drop(columns = ["gender"], inplace = False)
    
    for paciente, sexo in zip(df.index, lista_sexo):
        lista_quantidade_dias.append(__contagem_dias_creatinina_alta(df.loc[paciente], sexo))
    
    return lista_quantidade_dias
