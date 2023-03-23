# import of external modules;
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import sklearn
import imblearn 
import pickle

nltk.download("punkt")


# Import own modules;
from modules import CrearSentiment 
from modules import DropDuplicated
from modules import FillNa
from modules import UnirColumnas
from modules import FeatureSelection
from modules import stemfrases
from modules import Stemmer_English

# ----------------------------------------------

# Import and define variable model with pickle, model_prueba.pkl;
# with open('./model_prueba.pkl', 'rb') as model:
#     model_1 = pickle.load(model)

# Import and define variable model with pickle, model_prueba.pkl;
with open('./best_model.pkl', 'rb') as model:
    model_1 = pickle.load(model)

# Título de la página;
st.title("Feelings predictor NLP")

# Seteo una explicación de la página;
st.write('Para que la predicción de los sentimientos del comentario sea exitosa, rellena, en inglés, el primer campo con el título del comentario, y en el segundo, un texto de comentario más desarrollado.')

# Prueba input review summary; 
summary = st.text_input(label='Título de tu review.', placeholder='Ingresa el título de tu review.', label_visibility='hidden')

# Prueba text area component;
text = st.text_area(label='Comentario', placeholder='Ingresa tu comentario desarrollado.', max_chars=200, label_visibility='hidden')

# Agrego un botón para que al darle click, hacer la predicción;
button = st.button('Predict')




if button:
    # Test data;
    prediction = model_1.predict(pd.DataFrame.from_dict({'Summary': [summary], 'Text': [text]}))

    prediction_text = 'Para realizar las predicciones hemos desarrollado un algoritmo que ha sido entrenado con 50 mil datos reales de Amazon, el mejor score obtenido es de 0.95'

    if prediction[0] == 0:

        st.write(prediction_text)
        st.write('Nuestro super predictor detectó que tu comentario puede ser representado con el siguiente emoji: contentx :wink:')
        # st.write(':unamused:')

    elif prediction[0] == 1:

        st.write(prediction_text)
        st.write('Nuestro super predictor detectó que tu comentario puede ser representado con el siguiente emoji: enojado :unamused:')



