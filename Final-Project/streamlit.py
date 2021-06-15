import streamlit as st
from PIL import Image
import src.manage_data as dat
#import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components
import src.manage_data as dat
from collections import Counter
#import src.cleaning as cl


image = Image.open("./images/mapa-comunidad-madrid.jpeg")
st.image(image)

st.write("""
# 2021 Madrid elections: Analysis of the most repeated words in programs of political parties and their potential influence of Spanish public broadcaster TVE
""")

party = st.selectbox("Select a political party", dat.party_list())

st.dataframe(dat.select_party(party))
data = dat.select_party(party)
st.bar_chart(data)
    
for p in dat.word_clouds[party][:3]:
    nombre = (p.split("/")[-1][:-4].replace("_", " ").capitalize())
    st.write(nombre)  
    st.image(Image.open(p)) 
    
st.write("""
#### Most used words in TVE news programs regarding the party and the candidate during the campaign 
""")

st.dataframe(dat.select_verba(party))
data = dat.select_verba(party)
st.bar_chart(data)


st.image(Image.open(dat.word_clouds[party][3]))

palabra = st.text_input("Insert the word you want to check in the program", "Sanidad")

data = dat.get_program_part(party, palabra)

st.table(data)

    