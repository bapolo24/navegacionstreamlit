import streamlit as st  # Importa la librería Streamlit con el alias st.
inicio = st.Page("inicio.py", title="Inicio", icon="🏠", default=True)  # Define la página principal.
api = st.Page("api.py", title="Grado API", icon="🛢️")  # Define la página de la calculadora.
pagina = st.navigation([inicio, api])  # Registra las páginas disponibles dentro de la app.
pagina.run()  # Ejecuta la página seleccionada en la navegación.
