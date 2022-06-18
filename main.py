import streamlit as st
import pandas as pd
from home import sekolah_home
from home import siswa_home
from moora import metodeMoora
from streamlit_option_menu import option_menu
import sqlite3
conn = sqlite3.connect('beasiswa.db', check_same_thread=False)
c = conn.cursor()

# Fungsi untuk eksekusi query sql database
def login_user(email, password):
    c.execute('SELECT * FROM users WHERE email = ? AND password=?', (email, password))
    data = c.fetchall()
    return data

def edit_password_handler(email, currentPassword, newPassword):
    c.execute('SELECT * FROM users WHERE email = ? AND password=?', (email, currentPassword))
    data = c.fetchall()
    if data:
        c.execute('UPDATE users SET password=? WHERE email=?', (newPassword, email))
        conn.commit()
        st.success("Berhasil Edit Password")
    else:
        st.error("email dan password salah") 
        
# Membuat section container halaman
headerSection = st.container()
loginSection = st.container()
logOutSection = st.container()
sidebarSection = st.container()
mainSection = st.container()
editPasswordSection = st.container()
inputSection = st.container()

def show_sidebar():
    if st.session_state['role'] == 'siswa':
        menu = ['Home', 'Pengumuman', 'Edit Password']
    else:
        menu = ['Home', 'Input', 'Hasil', 'Edit Password']
    with sidebarSection:
        with st.sidebar:
            selected = option_menu(
                menu_title = 'Main Menu',
                options=menu,
            )
    
        if selected == "Home":
            show_main_page()  
        elif selected == "Input":
            input_page()
        elif selected == "Hasil":
            st.title("Hasil")
        elif selected == "Edit Password":
            edit_password_page()

def show_main_page():
    with mainSection:
        if st.session_state['role'] == 'siswa':
            siswa_home()
        else:
            sekolah_home()
        
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.sidebar.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            st.subheader("Login Section")
    
            email = st.text_input("Email : ")
            password = st.text_input("Password", type='password')
            if st.button("Login"):
                result = login_user(email, password)
                if result:
                    st.session_state['loggedIn'] = True
                    st.success("Logged In As {}".format(result[0][1])) 
                    st.session_state['role'] = result[0][4]
                else:
                    st.session_state['loggedIn'] = False
                    st.error('email dan password salah')
                    
def input_page():
    with inputSection:
        st.subheader("Input Data CSV")
        uploaded_file = st.file_uploader("Choose CSV file", type=['csv'])
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
            
            if st.button("Analisis MOORA"):
                hasil = metodeMoora(dataframe)
                st.download_button(label='Download Hasil CSV', data=hasil.to_csv(index=False), file_name="output.csv", mime='text/csv')
                    
def edit_password_page():
    with editPasswordSection:
        st.subheader("Edit Password")
        
        email = st.text_input("Email : ")
        currentPassword = st.text_input("Current Password", type='password')
        newPassword = st.text_input("New Password", type='password')
        if st.button("Edit"):
            edit_password_handler(email, currentPassword, newPassword)

with headerSection:
    st.title("Sistem Penentuan Beasiswa SMKN 1 Ciomas Kabupaten Bogor")

    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        st.session_state['role'] = ''
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()
            show_sidebar()    
        else:
            show_login_page()