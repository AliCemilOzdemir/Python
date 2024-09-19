#!/usr/bin/env python
# coding: utf-8
#dosyayı py olarak kaydet ve komut satırını kullanarak streamlit run streamlit.py 
import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2
model=load_model('date_fruit_class_cnn.h5')
def process_image(img):
    img=img.resize((224,224))
    img=np.array(img)
    img=img[:,:, :3]  # Remove the alpha channel
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img
st.title('Date Fruit Classification')
st.write('Please choose an image so that the AI model can predict the type of date.')
file=st.file_uploader('Pick an image', type= ['jpg','jpeg','png'])
class_names=['Ajwa', 'Medjool','Nabtat Ali', 'Shaishe', 'Sugaey', 'Galaxy', 'Meneifi','Rutab', 'Sokari']   
if file is not None:
    img=Image.open(file)
    st.image(img,caption='The image: ')
    image=process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)
    st.write('Probability Distribution')
    st.write(prediction)
    st.write("Prediction: ",class_names[predicted_class])