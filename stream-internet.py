import pickle
import streamlit as st

# Membaca Model 
internet_model = pickle.load(open('internet_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi Pembayaran Internet')

# Membagi Kolom
col1, col2 = st.columns(2)

with col1 :
    TAGIHAN_BULANAN_JANUARI   = st.text_input ('Input Tagihan')

with col2 :
    BAYAR = st.text_input ('Input Pembayaran') 
    
with col1 :
    TANGGAL_BAYAR = st.text_input ('Input Tanggal Bayar')
    
with col2 :
    JENIS_KELAMIN = st.text_input ('Input Jenis  Kelamin')

# Code Untuk Prediksi 
inter_status = ''

# Membuat Tombol Untuk Prediksi
if st.button('Test Prediksi Pembayaran'):
    inter_prediction = internet_model.predict([[TAGIHAN_BULANAN_JANUARI, BAYAR, TANGGAL_BAYAR, JENIS_KELAMIN]])

    if(inter_prediction[0] == 1):
        inter_status = 'Tepat'
    else :
        inter_status = 'Terlambat'
    st.success(inter_status)