import numpy as np # librería para cálculo numérico
import pandas as pd # librería para análisis de datos

def normalizar(df,var:str,umbral:float=0.05)->tuple:
    """Esta función normaliza una variable discreta basada en el 
    principio de umbral de representatividad estadística.

    Args:
        df (pd.DataFrame): datos con v.d. a normalizar
        var (str): nombre de la variable
        umbral (float, optional): umbral estadístico deseado. Defaults to 0.05.

    Returns:
        tuple: nombre de la variable y mapa de normalización
    """
    aux = df[var].value_counts(1).to_frame() # frecuencias relativas
    aux['map'] = np.where(aux[var]<umbral,'Otros',aux.index) # mapa de normalización
    if aux.loc[aux['map']=='Otros'][var].sum()<umbral: # si el umbral no se cumple
        aux['map'].replace({'Otros':aux.head(1)['map'].values[0]},inplace=True) # se asigna a la categoría más frecuente
    aux.drop(var,axis=1,inplace=True)    # se elimina la columna de frecuencias relativas
    return var,aux['map'].to_dict()      # se retorna el nombre de la variable y el mapa de normalización

def freq(df,var:list):     # función para calcular las frecuencias de una variable
    if type(var)!=list: 
        var = [var]        # si la variable no es una lista, se convierte en una lista
    for v in var:          # se recorre la lista de variables
        aux = df[v].value_counts().to_frame().sort_index() # se calculan las frecuencias absolutas
        aux.columns = ['FA'] # se renombra la columna
        aux['FR'] = aux['FA']/aux['FA'].sum() # se calculan las frecuencias relativas
        aux[['FAA','FRA']] = aux.cumsum() # se calculan las frecuencias acumuladas absolutas y relativas
        print(f'****Tabla de frecuencias  {v}  ***\n\n') # se imprime el nombre de la variable
        print(aux) # se imprime la tabla de frecuencias
        print("\n"*3) # se imprime 3 saltos de línea


