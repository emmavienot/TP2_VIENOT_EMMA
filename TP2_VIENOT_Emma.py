# TP2 - Créer une application Streamlit

# CHARGEMENT DES LIBRAIRIES

import streamlit as st          # créer l'interface web interactive
import pandas as pd             # chargement et manipulation des données CSV
import plotly.express as px     # graphiques (2D - 3D)


# DEMANDER LE NOM DE L'UTILISATEUR
st.title("TP2 - Créer une application Streamlit")
st.markdown("Emma Vienot - 26/05/2026")

st.sidebar.header("Options")
st.sidebar.markdown("Demande de prénom")
nom = st.sidebar.text_input("Entrez votre prénom")
if nom:
    st.sidebar.success(f"Bonjour, {nom} !")


# CHARGEMENT DU FICHIER
# RECUPERATION DE LA LISTE DE COLONNE DU EXCEL

uploaded_file = st.file_uploader("choisir un fichier CSV", type = "csv")
if uploaded_file is not None:

    # récupération des données
    st.write("fichier importé avec succes !")
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # récupération des colonnes numériques
    colonnes_num = df.select_dtypes(include=["int64", "float64"]).columns

    st.write("Colonnes numériques :", list(colonnes_num))


# CHOIX AVEC SELECT-BOX
st.sidebar.markdown("choisir entre 2D et 3D")
graphe_type = st.sidebar.selectbox("type de dimension", ["2D", "3D", "aucun"])


# ANALYSE DES DONNEES EN 2D
if graphe_type != "aucun":

    # colonnes numériques
    colonnes_num = df.select_dtypes(include="number").columns

    if graphe_type == "2D":

        st.subheader("Graphique 2D")
        st.markdown("on peut choisir parmis nos trois colonnes " \
        "à quel axe entre X et Y nous voulons les assigner !")

        col_x = st.selectbox("Choisir l'axe X", colonnes_num)
        col_y = st.selectbox("Choisir l'axe Y", colonnes_num)

        st.line_chart(df[[col_x, col_y]])

# ANALYSE DES DONNEES EN 3D
    elif graphe_type == "3D":

        st.subheader("Graphique 3D")
        st.markdown("on peut choisir parmis nos trois colonnes " \
        "à quel axe entre X, Y et Z nous voulons les assigner !")

        col_x = st.selectbox("Choisir X", colonnes_num)
        col_y = st.selectbox("Choisir Y", colonnes_num)
        col_z = st.selectbox("Choisir Z", colonnes_num)

        df_clean = df[[col_x, col_y, col_z]].dropna()
        fig = px.scatter_3d(df, x=col_x, y=col_y, z=col_z)

        st.plotly_chart(fig, use_container_width=True)