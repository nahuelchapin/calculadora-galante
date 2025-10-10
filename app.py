import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(
    page_title="Calculadora Galante D'Antonio",
    page_icon="🚗",
    layout="centered"
)

# --- LOGO ---
st.image("logo_galante.jpeg", use_container_width=True)

st.markdown("""
<style>
    body {
        background-color: white;
    }
    .stButton>button {
        background-color: #e3b500;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("Calculadora de Interés de Suscripción")
st.write("*Galante D’Antonio - de D’Antonio & Soto*")
st.divider()

# --- DATOS DE INTERÉS ---
intereses = {
    2: 0.1162,
    3: 0.1640,
    4: 0.1832,
    5: 0.2237,
    6: 0.3381,
    7: 0.3079,
    8: 0.3517,
    9: 0.5369,
    10: 0.4425,
    11: 0.4897,
    12: 0.7460
}

# --- ENTRADAS ---
monto = st.number_input("Monto de suscripción ($)", min_value=0.0, step=1000.0, format="%.2f")
cuotas = st.selectbox("Cantidad de cuotas", list(intereses.keys()))

# --- CÁLCULO ---
if st.button("Calcular"):
    interes = intereses[cuotas]
    recargo = monto * interes
    total = monto + recargo
    valor_cuota = total / cuotas

    st.success("Resultado:")
    st.write(f"*Monto original:* ${monto:,.2f}")
    st.write(f"*Interés aplicado:* {interes*100:.2f}%")
    st.write(f"*Recargo:* ${recargo:,.2f}")
    st.write(f"*Total con recargo:* ${total:,.2f}")
    st.write(f"*Valor de cada cuota ({cuotas}):* ${valor_cuota:,.2f}")

st.divider()
st.caption("© Galante D’Antonio - Calculadora de financiación | Versión Streamlit 2025")
