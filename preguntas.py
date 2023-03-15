"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd
import numpy as np

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    num_filas = tbl0.shape[0]

    return num_filas


def pregunta_02():
    num_columnas = tbl0.shape[1]

    return num_columnas


def pregunta_03():
    df = pd.DataFrame(tbl0, columns=['_c1'])
    counts = df['_c1'].value_counts().sort_index()

    return counts


def pregunta_04():
    columna1 = tbl0['_c1']
    columna2 = tbl0['_c2']
    df_c1 = pd.DataFrame({'_c1': columna1})
    df_c2 = pd.DataFrame({'_c2': columna2})
    df = pd.concat([df_c1, df_c2], axis=1)
    promedios =df.groupby(['_c1'])['_c2'].mean()

    return promedios


def pregunta_05():
    columna1 = tbl0['_c1']
    columna2 = tbl0['_c2']
    df_c1 = pd.DataFrame({'_c1': columna1})
    df_c2 = pd.DataFrame({'_c2': columna2})
    df = pd.concat([df_c1, df_c2], axis=1)
    promedios =df.groupby(['_c1'])['_c2'].max()

    return promedios


def pregunta_06():
    mayuscula = sorted(tbl1['_c4'].str.upper().unique().tolist())
    return mayuscula


def pregunta_07():
    columna1 = tbl0['_c1']
    columna2 = tbl0['_c2']
    df_c1 = pd.DataFrame({'_c1': columna1})
    df_c2 = pd.DataFrame({'_c2': columna2})
    df = pd.concat([df_c1, df_c2], axis=1)
    suma_por_letra = df.groupby('_c1')['_c2'].sum()

    return suma_por_letra


def pregunta_08():
    df=pd.DataFrame(tbl0)
    df['suma']= df['_c0'] + df['_c2']

    return df


def pregunta_09():
    df=pd.DataFrame(tbl0)
    df['year']= df['_c3'].str.slice(0,4)
    
    return df


def pregunta_10():
    df=pd.DataFrame(tbl0)
    tabla= df.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()
    tabla = tabla.set_index('_c1')

    return tabla


def pregunta_11():
    df=pd.DataFrame(tbl1)
    tabla= df.groupby('_c0')['_c4'].apply(lambda x: ','.join(map(str, sorted(x)))).reset_index()
    
    return tabla


def pregunta_12():
    df=pd.DataFrame(tbl2)
    tabla = df.groupby('_c0').apply(lambda x: ','.join(f"{a}:{b}" for a, b in sorted(zip(x['_c5a'], x['_c5b']))))
    tabla = tabla.reset_index()
    tabla.columns = ['_c0', '_c5']

    return tabla


def pregunta_13():
    columna_co = tbl2['_c0']
    columna_c5b = tbl2['_c5b']

    concatenado = pd.concat([columna_co, columna_c5b.astype(str)], axis=1)
    concatenado['_c5b'] = concatenado.groupby('_c0')['_c5b'].transform(lambda x: ','.join(sorted(x)))
    concatenado = concatenado.drop_duplicates().set_index('_c0')

    col5 = concatenado['_c5b'].str.split(',', expand=True).fillna(0).astype('int')
    suma = col5.sum(axis=1)

    tbl0['_c5b'] = suma
    suma_total = tbl0.groupby('_c1')['_c5b'].sum()
    
    return suma_total
