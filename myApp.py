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
st.title("Feelings Predictor NLP")

prediction_text = 'Our algorithm was trained with 426.340 real Amazon product reviews. The model is 96% accurate with a 82% recall.';

st.write(prediction_text)

# Seteo una explicación de la página;
st.write('For a successfull sentiment prediction, please fill in a summary of the product review in the first field, and a detailed product review in the second field.')

# Prueba input review summary; 
summary = st.text_input(label='Summary ', placeholder='Summary.', label_visibility='hidden')

# Prueba text area component;
text = st.text_area(label='Detailed product review', placeholder='Detailed product review', max_chars=5000, label_visibility='hidden')

# Agrego un botón para que al darle click, hacer la predicción;
button = st.button('Predict')




if button:
    # Test data;
    prediction = model_1.predict(pd.DataFrame.from_dict({'Summary': [summary], 'Text': [text]}))

    if prediction[0] == 0:
        st.write('Our super sentiment analysis algorithm predicts that your product review is: :wink:')
        # st.write(':unamused:')

    elif prediction[0] == 1:
        st.write('Our super sentiment analysis algorithm predicts that your product review is: :unamused:')



