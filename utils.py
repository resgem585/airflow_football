
import pandas as pd
import time
import random
import os
from datetime import datetime

# Función que obtiene datos de una URL y agrega información sobre la liga
def get_data(url, liga):
    # Tiempo de espera aleatorio entre 1, 2 y 3 segundos
    tiempo = [1, 3, 2]
    time.sleep(random.choice(tiempo))

    # Lee las tablas HTML desde la URL y las concatena en un solo DataFrame
    df = pd.read_html(url)
    df = pd.concat([df[0], df[1]], ignore_index=True, axis=1)

    # Renombra las columnas para mayor claridad
    df = df.rename(columns={0: 'EQUIPO', 1: 'J', 2: 'G', 3: 'E', 4: 'P', 5: 'GF', 6: 'GC', 7: 'DIF', 8: 'PTS'})

    # Procesa el nombre del equipo para eliminar números iniciales (si los hay)
    df['EQUIPO'] = df['EQUIPO'].apply(lambda x: x[5:] if x[:2].isnumeric() == True else x[4:])

    # Agrega información sobre la liga y la fecha de ejecución
    df['LIGA'] = liga
    run_date = datetime.now().strftime("%Y-%m-%d")
    df['CREATED_AT'] = run_date

    return df

# Función que procesa datos de múltiples ligas y los concatena en un solo DataFrame
def data_processing(df):
    # Obtiene datos de diferentes ligas
    df_spain = get_data(df['URL'][0], df['LIGA'][0])
    df_premier = get_data(df['URL'][1], df['LIGA'][1])
    df_italy = get_data(df['URL'][2], df['LIGA'][2])
    df_germany = get_data(df['URL'][3], df['LIGA'][3])
    df_francia = get_data(df['URL'][4], df['LIGA'][4])
    df_portugal = get_data(df['URL'][5], df['LIGA'][5])
    df_holanda = get_data(df['URL'][6], df['LIGA'][6])

    # Concatena todos los DataFrames de ligas en uno solo
    df_final = pd.concat([df_spain, df_premier, df_italy, df_francia, df_portugal, df_holanda], ignore_index=False)

    return df_final