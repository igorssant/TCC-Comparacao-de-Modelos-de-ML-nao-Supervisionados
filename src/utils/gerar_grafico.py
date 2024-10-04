import sys
sys.path.append("./utils/")
from matplotlib import pyplot as plt
from PIL import Image
import pandas as pd
import io


def __gerar_grafico(dados_paciente:pd.DataFrame, paciente:str) -> io.BytesIO:
    buffer: io.BytesIO
    
    plt.figure(figsize = (8, 6))
    plt.plot(dados_paciente["dia"], dados_paciente["ureia"])
    plt.title(f"Paciente: {paciente}")
    plt.xlabel("Dias")
    plt.ylabel("Ureia")
    buffer = io.BytesIO()
    plt.savefig(buffer, format = "jpg")
    plt.close()
    
    return buffer.getvalue()

def gerar_dataframe_imagens_ureia(df:pd.DataFrame) -> pd.DataFrame:
    lista_imagens = []
    lista_pacientes:list[str] = df.index.to_list()
    
    for paciente in lista_pacientes:
        lista_imagens.append(
            __gerar_grafico(df, paciente)
        )
    
    dados:dict = {
        "subject_id" : lista_pacientes,
        "img_ureia" : lista_imagens
    }
    
    return pd.DataFrame(dados)
    