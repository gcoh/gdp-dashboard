import streamlit as st

st.title("Exemples de mise en page Streamlit")

# 1. Colonnes
st.header("1. Colonnes")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Colonne 1")
    st.button("Bouton 1")
with col2:
    st.write("Colonne 2")
    st.button("Bouton 2")
with col3:
    st.write("Colonne 3")
    st.button("Bouton 3")

# 2. Sidebar
st.header("2. Sidebar")
st.sidebar.write("Ceci est dans la sidebar")
st.sidebar.slider("Choisissez une valeur", 0, 100, 50)

# 3. Expander
st.header("3. Expander")
with st.expander("Cliquez pour voir plus"):
    st.write("Ce contenu est caché par défaut.")
    st.image("https://placekitten.com/200/300")

# 4. Containers
st.header("4. Containers")
container = st.container()
container.write("Ce contenu est dans un container.")
st.write("Ce contenu est en dehors du container.")
container.write("On peut ajouter du contenu au container plus tard.")

# 5. Tabs
st.header("5. Tabs")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Contenu de l'onglet 1")
with tab2:
    st.write("Contenu de l'onglet 2")
