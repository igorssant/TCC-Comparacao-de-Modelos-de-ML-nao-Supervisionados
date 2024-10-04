# SE ESTIVER UTILIZANDO ESTA CLASSE DE MANEIRA DIRETA
# EXCLUA AS LINHA 3 e 4
#
import sys
sys.path.append("./utils/")
from scipy.spatial.distance import pdist, squareform
import pandas as pd


def distancia_gower(x:pd.Series, y:pd.Series) -> list[float]:
    tamanho = len(x)
    distancia = 0
    
    for i in range(tamanho):
        if pd.isnull(x[i]) or pd.isnull(y[i]):
            distancia += 1
            
        elif isinstance(x[i], str) or isinstance(y[i], str):
            distancia += int(x[i] != y[i])
        
        else:
            distancia += abs(x[i] - y[i]) / max(abs(x[i]), abs(y[i]))
    
    return distancia / tamanho

def ajustar_distancias(dataframe:pd.DataFrame) -> list[float]:
    distances = pdist(dataframe, distancia_gower)
    
    return squareform(distances)
