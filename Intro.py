import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio2.jpg')
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://e487tvzsuvluweowgtrjlp.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Conversión de Imagen a Texto")
 image = Image.open('unnamed1.png')
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://ocr-audio-jmv5lbb3xvkt3kh3cmygxx.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Traductor de Audio")
 image = Image.open('unnamed.png')
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://shdksjdks-4gcjnnv6zdf5urwsw5nsje.streamlit.app/"
 st.write(f"Traductor de Audio: [Enlace]({url})")

with col2: 
 st.subheader("Reconocimiento de Imágenes")
 image = Image.open('image-3-2.png')
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://kkt9hzt2g6ridht6gxne5q.streamlit.app/"
 st.write(f"Reconocimiento de Imágenes: [Enlace]({url})")

 st.subheader("Giving up")
 image = Image.open('d086f56a4da1d8aedad7840d84273007.jpg')
 st.write("En el siguiete enlace vamos a ver una app acerca de rendirse completamente.") 
 url = "https://jjlopezp2-whatev-whatev-xq31nq.streamlit.app/"
 st.write(f"Give Up: [Enlace]({url})")


