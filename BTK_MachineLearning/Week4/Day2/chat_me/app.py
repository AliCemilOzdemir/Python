#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import google.generativeai as genai

genai.configure(api_key='API KEY ALIN')

st.title('Chat with Me')
model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

soru = st.text_input('Sen:')

if st.button('Sor'):
    response = chat.send_message(soru)
    st.write(response.text)
    st.write(chat.history)

if st.button('Yeni Sohbet'):
    chat = model.start_chat(history=chat.history)

