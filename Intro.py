import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones de Juan José López.")
  parrafo = (
    "Son apps que creé para Interfaces Multimodales en 2026-2."
  )
  st.write(parrafo)

col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Visión Artificial en Teachable Machine y YOLO")
 image = Image.open('fun-3d-cartoon-robot-illustration_183364-120131.avif')
 st.image(image, width=192)
 st.write("En el siguiente enlace, se podrá interpretar una imagen por medio de Keras y YOLO.") 
 url = "https://aaaaaaaaaaaa-cqfkrrvyeak8f9nf7pnwhk.streamlit.app/"
 st.write(f"Visión Artificial: [Enlace]({url})")

 st.subheader("Control de MQTT")
 image = Image.open('data-analysis-skills-duties-responsibilities.jpeg')
 st.image(image, width=192)
 st.write("En el siguiente enlace, se podrá controlar un Wokwi por medio de voz y MQTT.") 
 url = "https://bbbbbbbbbb-enqexgttkcky9akuphx5ad.streamlit.app/"
 st.write(f"Control de MQTT: [Enlace]({url})")

 st.subheader("Cerradura con Gestos")
 image = Image.open('hand_axis.png')
 st.image(image, width=192)
 st.write("En el siguiente enlace, se podrá abrir una cerradura por medio de gestos.") 
 url = "https://cerraduragestos-bxzbg5phzwtuuv7ofxmkmh.streamlit.app/"
 st.write(f"Cerradura Gestos: [Enlace]({url})")

with col2: 
  st.subheader("Control por Voz")
  image = Image.open('txt_to_audio2.jpg')
  st.image(image, width=200)
  st.write("En el siguiente enlace, se podrá abrir una puerta y prender luces por medio de voz.") 
  url = "https://ctrlvoice-natxxqqm3bxjuypk8szgaz.streamlit.app/"
  st.write(f"Control por voz: [Enlace]({url})")
  
  st.subheader("Tablero poco inteligente")
  image = Image.open('d086f56a4da1d8aedad7840d84273007.jpg')
  st.image(image, width=200)
  st.write("En el siguiete enlace una IA poco inteligente interpreta un dibujo.") 
  url = "https://drawrecog-zsek2gmvfrdz76h3qyvh9m.streamlit.app/"
  st.write(f"Tablero: [Enlace]({url})")
  
  st.subheader("Reconocimiento de Números")
  image = Image.open('cartoon-image-of-a-robot-reading-a-book-vector.jpg')
  st.image(image, width=200)
  st.write("En el siguiete enlace, una IA podrá reconocer números escritos a mano.") 
  url = "https://mnistpred-2gbn3g3fjbv7ety7w7uxri.streamlit.app/"
  st.write(f"Números: [Enlace]({url})")

with col3:
  st.subheader("Interpretación de Imágenes")
  image = Image.open('image-3-2.png')
  st.image(image, width=200)
  st.write("En el siguiente enlace, una IA interpretará una imagen.") 
  url = "https://visionapp-sk22vfwkub9aajjuwnq7ww.streamlit.app/"
  st.write(f"Nube de Palabras: [Enlace]({url})")

  st.subheader("Análisis de Sentimiento")
  image = Image.open('unnamed1.png')
  st.image(image, width=200)
  st.write("En el siguiente enlace, se podrá analizar la polaridad emocional de un texto.") 
  url = "https://sentimenta-qswjzjsgtmxnbpqp4mklcr.streamlit.app/"
  st.write(f"Análisis de Sentimiento: [Enlace]({url})")

  st.subheader("Tablero de Dibujo")
  image = Image.open('hand_axis.png')
  st.image(image, width=200)
  st.write("En el siguiete enlace se podrá dibujar en un tablero customizable.") 
  url = "https://3buapnn55j5dfiojuuwyk7.streamlit.app/"
  st.write(f"Tablero: [Enlace]({url})")
