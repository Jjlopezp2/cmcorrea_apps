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
 st.image(image, width=192)
 st.write("En el siguiente enlace, se convertirá un texto a audio.") 
 url = "https://e487tvzsuvluweowgtrjlp.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Conversión de Imagen a Texto")
 image = Image.open('unnamed1.png')
 st.image(image, width=192)
 st.write("En el siguiente enlace, se podrá convertir imágenes a texto.") 
 url = "https://ocr-audio-jmv5lbb3xvkt3kh3cmygxx.streamlit.app/"
 st.write(f"Imagen a Texto: [Enlace]({url})")

 st.subheader("Traductor de Audio")
 image = Image.open('unnamed.png')
 st.image(image, width=192)
 st.write("En el siguiente enlace, se podrá traducir un audio a otro idioma.") 
 url = "https://shdksjdks-4gcjnnv6zdf5urwsw5nsje.streamlit.app/"
 st.write(f"Traductor de Audio: [Enlace]({url})")

with col2: 
 st.subheader("Reconocimiento de Imágenes")
 image = Image.open('image-3-2.png')
 st.image(image, width=200)
 st.write("En el siguiente enlace, se podrán reconocer objetos de un ambiente.") 
 url = "https://kkt9hzt2g6ridht6gxne5q.streamlit.app/"
 st.write(f"Reconocimiento de Imágenes: [Enlace]({url})")

 st.subheader("Giving up")
 image = Image.open('d086f56a4da1d8aedad7840d84273007.jpg')
 st.image(image, width=200)
 st.write("En el siguiete enlace vamos a ver una app acerca de rendirse completamente.") 
 url = "https://jjlopezp2-whatev-whatev-xq31nq.streamlit.app/"
 st.write(f"Give Up: [Enlace]({url})")


