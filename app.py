import streamlit as st
import pickle

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from PIL import Image

with open('appendices/app/model.pkl', mode='rb') as pickle_in:
    pipe = pickle.load(pickle_in)
    
with open('appendices/app/tvec.pkl', mode='rb') as tvec_in:
    tvec = pickle.load(tvec_in)   

def classifier(user_text, user_prob):
    X_test = pd.DataFrame([user_text], columns=['unst_simp_lem'])
    X_test_tv = pd.DataFrame(tvec.transform(X_test['unst_simp_lem']).todense(), columns = tvec.get_feature_names())
    
    st.markdown('Scanned Text:  **' + user_text + '**')
    st.markdown('Probability Threshold:  **'  + str(user_prob) + '**')
    if pipe.predict_proba(X_test_tv)[0][1] >= user_prob:
        st.markdown('Given this probability threshold, the above text **does** seem to include subject matter related to suicidality.')
    else:
        st.write('Given this probability threshold, the above text **does not** seem to include subject matter related to suicidality.')

image = Image.open('images/aboutme.png')
sp = Image.open('images/suicideprevention.png')
nimh = Image.open('images/nimh.jpeg')
        
#Image.open('old.jpeg').convert('RGB').save('new.jpeg')
    
page = st.sidebar.selectbox(
'Select a Page', ('Home', 'About', 'Resources')
)

if page == 'Home':
    st.title('Suicidality Subject Matter Detection')
    
    user_text = st.text_input('Input text in the field below: ',
    value = "")
    
    user_prob = st.text_input('User may define custom value between 0 and 1 as the probability threshold ' +
    'equal to or beyond which a block of text will be classified as positive. Input custom threshold: ',
    value = "")
    
    if st.button('Scan Text'):
        classifier(user_text, float(user_prob))
    
if page == 'About':
    st.title('About the Creator')
    st.image(image, caption = 'Brian Berry', width = 200)
    st.markdown('As a data scientist, Brian finds the stories behind numbers. With a background in the humanities and extensive experience in cross-team IT environments, his hope is to use his skills in analytics/statistical modeling and technical communication to help teams and individuals thrive.')
    
if page == 'Resources':
    st.title('Additional Resources')
    st.image(sp, caption = 'https://www.sprc.org', width = 125)
    st.image(nimh, caption = 'https://www.nimh.nih.gov', width = 125)