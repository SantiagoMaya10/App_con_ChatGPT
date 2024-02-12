# Importar librerías necesarias
import streamlit as st

# Título y autor de la app
st.write("# Mi primera app")
st.write("Esta app fue elaborada por Luis Santiago Maya Restrepo")

# Pedir al usuario su nombre
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Mostrar mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
