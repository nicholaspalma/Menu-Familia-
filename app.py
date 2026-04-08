import streamlit as st
import pandas as pd
import time

# 1. Configuración de página (Debe ir primero)
st.set_page_config(page_title="App Familia", page_icon="📱", layout="centered")

# 2. Inyección de CSS para hacerlo más moderno (estilo App)
st.markdown("""
    <style>
        .main { background-color: #f8fafc; }
        h1 { color: #4f46e5; font-weight: 800; }
        h2 { color: #334155; font-weight: 700; }
        .stProgress > div > div > div > div { background-color: #10b981; }
        .resumen-caja { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
    </style>
""", unsafe_allow_html=True)

# 3. Título Principal
st.title("👨‍👩‍👧 Familia: Francisca, Nicholas & Josefa")
st.caption("Gestiona tu menú, alacena y presupuesto familiar en un solo lugar.")

# 4. Navegación Moderna
tab_menu, tab_finanzas, tab_escaner = st.tabs(["🍽️ Menú & Alacena", "💰 Presupuesto", "📷 Escáner de Boletas"])

# --- PESTAÑA 1: MENÚ Y ALACENA ---
with tab_menu:
    st.markdown("### ¿Qué comemos hoy, Martes?")
    
    # Tarjeta moderna del menú diario
    col_menu1, col_menu2 = st.columns([2, 1])
    with col_menu1:
        st.success("**Almuerzo:** Lentejas con Arroz 🍛")
        st.info("👶 **Josefa:** Porción pequeña, texturas separadas.")
    with col_menu2:
        st.warning("**Desayuno Mañana:**\n\nYogurt con Cereal 🥣")

    st.markdown("---")
    st.markdown("### 📦 Stock Rápido (Alacena)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Sofritos", "1 bolsa", "-1 (Crítico)", delta_color="inverse")
    col2.metric("Carne Molida", "800g", "Ok", delta_color="normal")
    col3.metric("Lentejas", "250g", "Bajo", delta_color="inverse")

# --- PESTAÑA 2: PRESUPUESTO ---
with tab_finanzas:
    st.markdown("### Control de Gastos del Mes")
    
    presupuesto_total = 200000
    gasto_actual = 85400
    porcentaje = int((gasto_actual / presupuesto_total) * 100)
    
    st.markdown(f"**Has gastado ${gasto_actual:,} de ${presupuesto_total:,}**")
    st.progress(porcentaje)
    
    col_gasto1, col_gasto2 = st.columns(2)
    col_gasto1.metric("Disponible", f"${(presupuesto_total - gasto_actual):,}")
    col_gasto2.metric("Ahorro estimado", "$12.000")
    
    st.markdown("#### Últimas Compras")
    gastos_data = pd.DataFrame({
        "Fecha": ["01/04", "04/04"],
        "Lugar": ["Feria (Verduras)", "Supermercado (Quincenal)"],
        "Monto": ["$15.000", "$70.400"]
    })
    st.dataframe(gastos_data, use_container_width=True, hide_index=True)

# --- PESTAÑA 3: ESCÁNER DE BOLETAS ---
with tab_escaner:
    st.markdown("### 📸 Inteligencia Artificial")
    st.write("Sube la foto de la boleta y extraeremos los productos para actualizar tu despensa y tus gastos.")
    
    boleta_img = st.file_uploader("Tomar foto o subir boleta", type=["jpg", "png", "jpeg"])
    
    if boleta_img is not None:
        st.image(boleta_img, caption="Boleta cargada", use_column_width=True)
        
        if st.button("🔍 Escanear y Extraer Datos", type="primary"):
            # Simulamos el tiempo de procesamiento de la IA
            with st.spinner("La IA está leyendo la boleta..."):
                time.sleep(3) # Espera 3 segundos simulando pensar
            
            st.success("¡Datos extraídos con éxito!")
            
            # Tabla interactiva (Data Editor es súper moderno)
            st.markdown("#### Productos Detectados (Puedes editar si hay errores)")
            productos_extraidos = pd.DataFrame({
                "Producto": ["Pollo Pechuga", "Sofrito Congelado", "Yogurt Natural", "Arroz Tucapel"],
                "Cantidad": [2, 3, 6, 1],
                "Unidad": ["Bandejas", "Bolsas", "Unidades", "Kg"],
                "Precio Total": [12000, 4500, 3000, 1800]
            })
            
            # data_editor permite al usuario modificar la tabla en vivo
            df_editado = st.data_editor(productos_extraidos, use_container_width=True, hide_index=True)
            
            total_boleta = df_editado["Precio Total"].sum()
            st.metric("Total Detectado", f"${total_boleta:,}")
            
            st.button("✅ Confirmar y Guardar en Alacena")
