import streamlit as st
import requests

st.set_page_config(page_title="Generador de Posts con IA")


col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=200)

st.title("Generador de Posts para Redes Sociales con IA")
st.write("Completá los datos para generar tu contenido 👇")

rubro = st.text_input("¿De qué es tu negocio?")
tipo_post = st.selectbox("Tipo de post", ["Promoción", "Educativo", "Historia"])
objetivo = st.text_input("¿Cuál es el objetivo del post?")

API_KEY = st.secrets["API_KEY"]

def generar_post(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {e}"


if st.button("Generar post"):
    if rubro and objetivo:

        prompt = f"""
Actuá como un experto en marketing digital.

Generá un post de Instagram para un emprendimiento de {rubro} en Argentina.

Tipo de post: {tipo_post}
Objetivo: {objetivo}

Debe incluir:
- tono cercano
- llamada a la acción
- hashtags

Separar en:

POST:
HASHTAGS:
"""

        resultado = generar_post(prompt)

        st.subheader("Resultado:")
        st.write(resultado)

    else:
        st.warning("Completá todos los campos")