import streamlit as st
import eda
# import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Graded Challenge 7')
    st.write('Nama      : Syihabuddin Ahmad Satisma')
    st.write('Batch     : HCK-017')
    st.write('Tujuan GC7    : Membuat NLP berdasarkan klasifikasi binary pada target label antara positive review ataupun negative review')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Latar belakang dalam penelitian ini adalah untuk memprediksi sebuah teks apakah teks tersebut termasuk ke dalam positive review atau negative review')

    with st.expander("Problem Statement"):
            st.caption('Model diharapkan dapat memprediksi suatu kata sesuai klasifikasinya')

    with st.expander("Kesimpulan"):
        st.caption('Model sudah dapat memprediksi kata dengan accuracy total 82%. Maaf mas saya masih belum mengerti cara mendeploy ke streamlit maupun hugging face untuk model NLP jadi masih terkendala error dalam model prediksi.')
elif page == 'Exploration Data Analysis':
    eda.run()
# else:
#      models.run()