import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuración de la página
st.set_page_config(
    page_title="App Familiar", 
    page_icon="🏡", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Título personalizado
st.title("🏡 Familia: Francisca, Nicholas y Josefa")
st.markdown("---")

# 3. Navegación usando pestañas (Tabs)
tab1, tab2, tab3 = st.tabs(["🍽️ Menú Diario", "📦 Alacena", "🧾 Escanear Boleta"])

with tab1:
    st.header("¿Qué comemos hoy?")
    
    # Tarjeta de menú de ejemplo
    st.success("**Almuerzo de hoy:** Lentejas con Arroz 🍲")
    st.info("**Para Josefa (2 años):** Lentejas procesadas suave + Arroz separado")
    st.warning("**Desayuno de mañana:** Yogurt con Cereal 🥣")
    
    st.markdown("### Plan de la Semana")
    # Una tabla simple simulando el menú
    menu_data = {
        "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
        "Almuerzo": ["Pasta con carne", "Lentejas con arroz", "Arroz con pollo", "Puré con carne", "Pastelera de pollo"]
    }
    df_menu = pd.DataFrame(menu_data)
    st.dataframe(df_menu, use_container_width=True, hide_index=True)

with tab2:
    st.header("Estado de la Alacena")
    # Simulando el stock
    col1, col2 = st.columns(2)
    col1.metric(label="Sofritos Congelados", value="2 bolsas", delta="-1 usada ayer")
    col2.metric(label="Carne Molida", value="800 g", delta="Stock óptimo", delta_color="normal")
    
    st.button("Actualizar Alacena manualmente")

with tab3:
    st.header("Cargar Compras")
    st.markdown("Próximamente conectaremos la Inteligencia Artificial aquí.")
    boleta = st.file_uploader("Sube una foto de la boleta del supermercado", type=["jpg", "png", "jpeg"])
    
    if boleta is not None:
        st.success("¡Foto cargada! Lista para ser analizada.")

# Footer
st.markdown("---")
st.caption("Desarrollado con ❤️ para organizar el hogar.")
