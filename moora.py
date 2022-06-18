import streamlit as st
import pandas as pd
import numpy as np

def metodeMoora(dataframe):
    st.write("### Normalisasi Data")
    data = dataframe.iloc[2:,1:].values
    kriteria = dataframe.columns.values
    bobot = dataframe.iloc[1, 1:].values
    atribut = dataframe.iloc[0, 1:].values
                
    # Menghitung normalisasi 
    data_norm = data.copy()
    data_norm = data_norm.astype('float64')
    for i in range(data.shape[0]):
        for j in range(data.shape[1]): 
            data_norm[i,j] = data[i,j] / np.sqrt(np.sum(data[:,j] ** 2))       
    df_norm = pd.DataFrame(data_norm, columns=kriteria[1:])
    st.dataframe(df_norm)
                
    # Menghitung nilai optimasi (w x r)
    st.write("### Nilai Optimasi (w x r)")
    data_optimasi = data.copy()
    data_optimasi = data_optimasi.astype('float64')
    for i in range(data_norm.shape[0]):
        for j in range(data_norm.shape[1]):
            data_optimasi[i,j] = data_norm[i,j] * bobot[j]
    df_optimasi = pd.DataFrame(data_optimasi, columns=kriteria[1:])
    st.dataframe(df_optimasi)
    
    # Menghitung Yi
    
    # Perangkingan
    
    return df_optimasi # return datanya menggunakan data hasil moora yang telah di ranking