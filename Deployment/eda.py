import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv(r'movie_trim.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn pie chart
    st.title('Pie Chart Label Distribution')
    image = Image.open('Eda1.png')
    st.image(image, caption='Label Distribution')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan pie chart di atas, dataset sudah memiliki distribusi yang balance')

#menampilakn wordcloud
    st.title('Positive Review Wordcloud Distribution')
    image = Image.open('Eda2.png')
    st.image(image, caption='Positive Wordcloud')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Wordcloud di atas adalah wordcloud pada label positive review')

#menampilakn wordcloud
    st.title('Negative Wordcloud Distribution')
    image = Image.open('Eda3.png')
    st.image(image, caption='Negative Wordcloud')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Wordcloud di atas adalah kata yang terdapat pada label negative review')

#menampilkan penjelasan 
    with st.expander('Kesimpulan EDA'):
        st.caption('Distribusi data antara positif sentiment dengan negatif sentiment sudah balance karena didapatkan bahwa data yang terbagi adalah 50.8% (negative sentiment) vs 49.2% (positive sentiment) dengan demikian persebaran target data sudah termasuk balance. Sentiment antara positive dan negative memiliki kesamaan pada teks yang besar.')




