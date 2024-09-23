import streamlit as st
import pandas as pd


# Titre de l'application
st.title("Ma première application Streamlit")

# Ajout d'un texte
st.write("Bienvenue dans cette démo!")

# Création d'un slider
age = st.slider("Quel est votre âge?", 0, 100, 25)
st.write("Vous avez", age, "ans")

# Création d'un dataframe exemple
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

# Affichage du dataframe
st.dataframe(df)
