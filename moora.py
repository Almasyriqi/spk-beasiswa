import streamlit as st
import pandas as pd
import numpy as np

def metodeMoora(dataframe ):
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
    temp_max = [0] * data_optimasi.shape[0]
    temp_min = [0] * data_optimasi.shape[0]

    for y in range(data_optimasi.shape[1]):
        for x in range(data_optimasi.shape[0]):
            if (atribut[y] == 1):
                temp_max[x] += data_optimasi[x,y]
            else:
                temp_min[x] += data_optimasi[x,y]

    result_yi = [0] * data_optimasi.shape[0]
    for i in range(data_optimasi.shape[0]):
        result_yi[i] = temp_max[i] - temp_min[i]
    
    # Perangkingan
    list_alternatif = dataframe.iloc[2:,0].values
    nilai = np.stack((list_alternatif, result_yi), axis=1)
    rank = list(range(1,list_alternatif.shape[0]+1))
    df_ranking = pd.DataFrame(nilai, columns=['Alternatif', 'Yi'])
    df_ranking = df_ranking.sort_values("Yi", ascending=False)
    df_ranking['Ranking'] = rank
    
    st.write("### Hasil Perangkingan Metode MOORA")
    st.dataframe(df_ranking)
    
    return df_ranking # return datanya menggunakan data hasil moora yang telah di ranking