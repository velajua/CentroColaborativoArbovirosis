import streamlit as st

### CORRE USANDO 'streamlit run ejemplos_streamlit.py'

# Título
st.title("Guía de Funciones de Streamlit")

# Encabezado
st.header("Encabezado")

# Subencabezado
st.subheader("Subencabezado")

# Texto
st.text("Este es un texto simple.")

# Texto enriquecido (Markdown)
st.markdown("### Texto enriquecido con Markdown")

# Agregar imagen
# from PIL import Image
# image = Image.open("imagen.jpg")
# st.image(image, caption="Una imagen")

# Agregar video
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"
st.video(video_url)

# Agregar audio
# audio_file = open("cancion.mp3", "rb")
# st.audio(audio_file, format="audio/mp3")

# Barra lateral
sidebar_value = st.sidebar.selectbox("Selecciona una opción", ["Opción 1", "Opción 2", "Opción 3"])
st.sidebar.text(f"Seleccionaste: {sidebar_value}")

# Entrada de texto
user_input = st.text_input("Ingresa tu nombre", "Ejemplo")

# Botón
if st.button("Haz clic"):
    st.text("¡Botón presionado!")

# Checkbox
checkbox_state = st.checkbox("Marcar esta casilla")
if checkbox_state:
    st.text("Casilla marcada")

# Selectbox (Dropdown)
option = st.selectbox("Elige una opción", ["Opción 1", "Opción 2", "Opción 3"])
st.text(f"Elegiste: {option}")

# Slider
slider_value = st.slider("Elige un valor", 0, 100, 50)
st.text(f"Valor seleccionado: {slider_value}")

# Gráfico de línea
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
st.line_chart(list(zip(x, y)))

# Gráfico de barras
data = {"Manzanas": 10, "Naranjas": 5, "Plátanos": 7}
st.bar_chart(data)

# Mapa
map_data = {
    "lat": [37.7749, 34.0522, 40.7128],
    "lon": [-122.4194, -118.2437, -74.0060],
    "name": ["San Francisco", "Los Angeles", "Nueva York"]
}
st.map(map_data)

# DataFrame
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.dataframe(df)

# Tabla
st.table(df)

# Expander
with st.expander("Ver más"):
    st.text("Contenido expandido aquí.")

# Cache
@st.cache_data
def expensive_computation():
    st.text("Realizando cálculo costoso...")
    return 42
result = expensive_computation()
st.text(f"Resultado: {result}")
