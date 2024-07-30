# Streamlit app
import streamlit as st
import pandas as pd
import re
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pickle
import warnings

# ignore warnings
warnings.filterwarnings('ignore')

# download necessary nltk data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# load vectorization data
vectorization_data = pickle.load(open('text_vectorization.pkl', 'rb'))
vectorizer = TextVectorization.from_config(vectorization_data['config'])
vectorizer.set_weights(vectorization_data['weights'])

# load model
model = tf.keras.models.load_model('model.h5')

# Define stopword
en_sword = list(set(stopwords.words('english')))
en_sword.extend(['dont', 'br', 'cant', 'isnt'])

# Define lemmatizer
lemmatizer = WordNetLemmatizer()

# create a function for text preprocessing
def text_preprocessing(text):
    # case folding
    text = text.lower()

    # mention removal
    text = re.sub("@[a-za-z0-9_]+", " ", text)

    # hashtags removal
    text = re.sub("#[a-za-z0-9_]+", " ", text)

    # newline removal (\n)
    text = re.sub(r"\\n", " ", text)

    # whitespace removal
    text = text.strip()

    # url removal
    text = re.sub(r"http\s+", " ", text)
    text = re.sub(r"www.\s+", " ", text)

    # non-letter removal (such as emoticon, symbol (like μ, $, 兀), etc
    text = re.sub("[^a-za-z\s']", " ", text)
    text = re.sub("'", "", text)

    # tokenization
    tokens = word_tokenize(text)

    # stopwords removal
    tokens = [word for word in tokens if word not in en_sword]

    # lemmatizing
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # combining tokens
    text = ' '.join(tokens)

    return text

# Streamlit app
def main():
    st.title('Sentiment Analysis App')
    st.write("Enter text to analyze its sentiment.")

    # User input
    user_input = st.text_area("Enter your text here:")

    if st.button("Predict"):
        # Clean and preprocess text
        clean_input = text_preprocessing(user_input)
        data_vect = vectorizer([clean_input])

        # Predict sentiment
        predicted_result_proba = model.predict(data_vect)

        # Show result
        predict_result = ''
        threshold = 0.5
        if predicted_result_proba[0] > threshold:
            predict_result = 'Positive'
        else:
            predict_result = 'Negative'

        st.write(f"Predicted Sentiment Probability: {predicted_result_proba[0]}")
        st.write(f"Predicted Sentiment: {predict_result}")

if __name__ == "__main__":
    main()
