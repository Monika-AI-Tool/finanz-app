import streamlit as st
import numpy_financial as npf
import pandas as pd

st.set_page_config(page_title="Finanzszenarien-Rechner", page_icon="💰", layout="wide")

st.markdown("""
# 💡 Finanzszenarien-Analyse-Tool

Willkommen! Dieses Tool hilft dir dabei, verschiedene Investitionsszenarien zu analysieren – inklusive **NPV** & **IRR**.

🔹 **Base Case**, **High Case**, **Low Case** vergleichen  
🔹 Cashflows und Zinssatz anpassen  
🔹 Ergebnisse visuell darstellen
---
""")

discount_rate = st.slider("📉 Diskontierungszinssatz (%)", 0.0, 20.0, 8.0) / 100

szenarien = {
    "Low Case": [-100000, 20000, 25000, 30000, 30000],
    "Base Case": [-100000, 25000, 30000, 35000, 40000],
    "High Case": [-100000, 30000, 35000, 40000, 45000]
}

daten = []
for name, cashflows in szenarien.items():
    npv = npf.npv(discount_rate, cashflows)
    irr = npf.irr(cashflows)
    daten.append({"Szenario": name, "NPV (€)": npv, "IRR (%)": irr * 100})

df = pd.DataFrame(daten)

st.subheader("📊 Vergleich der Szenarien")
st.dataframe(df.style.format({"NPV (€)": "€{:.2f}", "IRR (%)": "{:.2f}%"}), use_container_width=True)
st.bar_chart(df.set_index("Szenario")[["NPV (€)", "IRR (%)"]])

st.success("Berechnung abgeschlossen! 🎯")
