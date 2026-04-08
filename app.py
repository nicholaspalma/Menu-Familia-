import streamlit as st
import pandas as pd
from datetime import date
import time

# 1. CONFIGURACIÓN DE PÁGINA (Debe ir primero)
# Usamos layout="wide" para aprovechar mejor el espacio en notebook y móvil
st.set_page_config(page_title="App Familia N|F|J", page_icon="🏡", layout="wide")

# 2. DISEÑO EXTREMO (CSS Personalizado)
# Aquí inyectamos colores, formas redondeadas y sombras para un look moderno
st.markdown("""
    <style>
        /* Fondo principal de la App (Gris muy suave) */
        .stApp { background-color: #f1f5f9; }

        /* Títulos principales (Índigo oscuro) */
        h1, h2 { color: #1e1b4b !important; font-weight: 800 !important; }
        
        /* Estilo para las "Tarjetas" modernas (Fondo blanco, bordes redondeados, sombra) */
        .css-1r6slb0, .stDataFrame, .stAlert, div[data-testid="stVerticalBlock"] > div:has(div.card) {
            background-color: white;
            padding: 1.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            border: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }

        /* Colores personalizados para métricas */
        [data-testid="stMetricValue"] { color: #4f46e5; font-weight: 700; }
        
        /* Botones modernos (Índigo) */
        .stButton>button {
            border-radius: 12px;
            background-color: #4f46e5;
            color: white;
            border: none;
            padding: 10px 20px;
            font-weight: 600;
        }
        .stButton>button:hover { background-color: #4338ca; color: white; }

        /* Estilo para el input del chat */
        .stChatInputContainer { border-radius: 15px; }

    </style>
""", unsafe_allow_html=True)

# 3. CABECERA DE LA APP
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title("🏡 Smart Home: N | F | J")
    st.caption(f"Gestión colaborativa del hogar • {date.today().strftime('%A, %d de %B')}")
with col_header2:
    # Un pequeño indicador visual de quiénes usan la app
    st.markdown("""
        <div style="display: flex; gap: 10px; justify-content: flex-end;">
            <div style="background-color: #e0e7ff; color: #4338ca; padding: 10px 15px; border-radius: 50%; font-weight: bold;">N</div>
            <div style="background-color: #fce7f3; color: #db2777; padding: 10px 15px; border-radius: 50%; font-weight: bold;">F</div>
            <div style="background-color: #fef3c7; color: #b45309; padding: 10px 15px; border-radius: 50%; font-weight: bold;">J</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. NAVEGACIÓN MODERNA (Tabs coloridos)
# Hemos añadido una pestaña de "Resumen Hoy" donde integramos el Chat y Pendientes
tab_resumen, tab_menu, tab_finanzas, tab_escaner = st.tabs(["🚀 Resumen Hoy", "🍔 Menú & Stock", "📉 Gastos", "📷 Escáner IA"])

# --- PESTAÑA RESUMEN (Chat y Tareas Compartidas) ---
with tab_resumen:
    col_res1, col_res2 = st.columns([1, 1.3])

    # COLUMNA IZQUIERDA: Menú de Hoy y Pendientes
    with col_res1:
        st.markdown("### 📅 Menú de Hoy (Martes)")
        st.success("**Almuerzo:** Lentejas cremosas con Arroz Tucapel 🍛")
        st.info("👶 **Josefa (2 años):** Porción separada (arroz solo, lentejas poco sazonadas)")
        
        st.markdown("---")
        
        # SECCIÓN PENDIENTES (Gestor colaborativo)
        st.markdown("### 📌 Pendientes Compartidos")
        st.write("Gestionen tareas rápidas aquí. Hagan check al completar.")
        
        # Simulación de lista (Need database for real persistence)
        pendientes_data = {
            "Tarea": ["Comprar Pañales Josefa Talla G", "Pagar Cuenta Luz (antes del 15)", "Reparar enchufe cocina (Papá)", "Agendar pediatra Josefa"],
            "Hecho": [False, True, False, False]
        }
        
        # data_editor es ideal para listas interactivas modernas
        st.data_editor(pd.DataFrame(pendientes_data), use_container_width=True, hide_index=True)
        st.text_input("+ Agregar nuevo pendiente...", placeholder="Ej: Falta Arroz integral")

    # COLUMNA DERECHA: Chat / Recados Compartidos
    with col_res2:
        st.markdown("### 📝 Notas & Recados de la Familia")
        st.write("Mensajes rápidos sincronizados entre tus dispositivos y los de Francisca.")
        
        # Contenedor visual del chat
        chat_container = st.container(height=350, border=False)
        
        with chat_container:
            # SIMULACIÓN MOCK DE MENSAJES (No persisten entre sesiones sin base de datos)
            # Usamos los componentes nativos de chat de Streamlit que son muy modernos
            with st.chat_message("Nicholas", avatar="🧑‍💻"):
                st.write("¡Ojo! Se acabó el arroz integral anoche, falta comprar.")
                st.caption("Hace 1 hora")

            with st.chat_message("Francisca", avatar="👩‍🍳"):
                st.write("Ok, lo anoto en pendientes. ¿Queda pollo para el Miércoles?")
                st.caption("Hace 30 mins")

            with st.chat_message("Nicholas", avatar="🧑‍💻"):
                st.write("Sí, queda una pechuga en el congelador ✅.")
                st.caption("Hace 5 mins")

        # Input real del chat (se ve abajo de la pantalla en móvil)
        st.chat_input("Escribe un mensaje o recado familiar...")

# --- RESTO DE PESTAÑAS (Keeping previous requested functionality but improving UI) ---
with tab_menu:
    st.markdown("### 📦 Stock Interactiva Alacena")
    st.write("Modifiquen cantidades directamente en la tabla.")
    pantry_data = pd.DataFrame({
        "Producto": ["Pollo", "Carne Molida", "Pasta", "Arroz Tucapel", "Sofrito", "Lentejas"],
        "Cantidad": [200, 800, 3, 0.2, 1, 250],
        "Unidad": ["g", "g", "Unidades", "Kg", "Bolsa", "g"],
        "Estado": ["Ok ✅", "Ok ✅", "Ok ✅", "⚠️ Crítico", "⚠️ Crítico", "Bajo 📉"]
    })
    st.data_editor(pantry_data, use_container_width=True, hide_index=True, disabled=["Producto", "Unidad", "Estado"])

with tab_finanzas:
    st.markdown("### Presupuesto Mensual (Abril)")
    g_total = 200000
    g_act = 98500
    p_gasto = int((g_act/g_total)*100)
    
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Gasto Actual", f"${g_act:,}")
    col_m2.metric("Disponible", f"${(g_total-g_act):,}", f"Presupuesto: ${g_total:,}")
    
    st.progress(p_gasto, text=f"Has gastado el {p_gasto}% del presupuesto")

with tab_escaner:
    st.markdown("### 📸 IA Escáner Boletas")
    # Previous code inside cards...
    # (Keeping previous logic but inside card)
    boleta_img = st.file_uploader("Tomar foto o subir boleta", type=["jpg", "png", "jpeg"])
    
    if boleta_img is not None:
        if st.button("🔍 Escanear y Extraer Datos", type="primary"):
            # Simulamos el tiempo de procesamiento de la IA
            with st.spinner("La IA está leyendo la boleta..."):
                time.sleep(3) # Espera 3 segundos simulando pensar
            
            st.success("¡Datos extraídos con éxito!")
            # ... (Resto de la lógica interactiva) ...
