import streamlit as st
import pandas as pd
import numpy as np
import sqlite3


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
    
    temp_max = []
    temp_min = []
    result_max = 0
    result_min = 0
    for x in range(data_optimasi.shape[0]):
        for y in range(data_optimasi.shape[1]):
            if (y == 0 or y == 3 or y == 4):
                result_max = result_max + data_optimasi[x,y]
            if(y == 1 or y == 2):
                result_min = result_min + data_optimasi[x,y]
        temp_max.append(result_max)
        temp_min.append(result_min)
        result_max = 0  
        result_min = 0

    result_yi = []
    for i in range(len(temp_max)):
        result_yi.append(temp_max[i] - temp_min[i])

    
    # Perangkingan
    list_alternatif = []
    for x in dataframe.iloc[2: , 0].values:
        list_alternatif.append(str(x))
    
    my_dict = dict()
    count = 0
    for value in result_yi:
        my_dict[list_alternatif[count]] = value
        count = count + 1
    
    perangkingan = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    
    
    #Hasil Perangkingan adalah array
    """
    [('Dimas Permana', 1.4471299133366142), 
    ('Gadis Idhani', 1.2667837633596557), 
    ('Abdul Hakim', 0.8248420251180635), 
    ('Indah Permata Sari', 0.7207325951250203), 
    ('Desi Ismiyati', 0.22541412860488075), 
    ('Ahmad Zaelani', -0.05904145136512051), 
    ('Faridz Dwi Nurfalah', -0.5131348172711157),
     ('Adi Wiguna', -1.2740132361032235), 
     ('Faisal Hidayat', -1.6432877090412217),
      ('Hariono Yusuf', -1.6432877090412217)]
    """
    
    return perangkingan # return datanya menggunakan data hasil moora yang telah di ranking