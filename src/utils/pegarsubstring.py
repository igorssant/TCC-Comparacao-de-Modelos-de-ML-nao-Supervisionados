import sys
sys.path.append("./utils/")
import pandas as pd

def substring(frase:str, separacao:str= "= ") -> str:
     try:
          frase = frase.split(separacao, 1)[1]
          frase = frase.split("\n")[0]
     
     except IndexError:
          frase = ""
          
     return frase

def renomear_series(serie:pd.Series, excluir:str) -> pd.Series:
     nova_serie:pd.Series = [valor.replace(excluir, "") for valor in serie]
     return nova_serie
