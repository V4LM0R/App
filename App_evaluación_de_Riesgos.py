import streamlit as st
import pandas as pd
import plotly.express as px

st.title('HERRAMIENTA DE EVALUACION DE RIESGOS')

uploaded_file = st.file_uploader("Elige un archivo de texto", type="txt")

if uploaded_file is not None:
   
    data = []
    for line in uploaded_file:
        decoded_line = line.decode("utf-8").strip()
        if decoded_line:
            data.append(decoded_line.split(','))

    df = pd.DataFrame(data, columns=["Riesgo", "Profesional", "Profesión", "Probabilidad", "Impacto"])

    st.write("Datos cargados:")
    st.write(df)

    st.header("Distribución de Probabilidad")
    fig_probabilidad = px.histogram(df, x='Probabilidad', title='Distribución de Probabilidad', color='Profesión')
    st.plotly_chart(fig_probabilidad)

    st.header("Distribución de Impacto")
    fig_impacto = px.histogram(df, x='Impacto', title='Distribución de Impacto', color='Profesión')
    st.plotly_chart(fig_impacto)

    st.header("Probabilidad vs Impacto")
    fig_prob_impacto = px.scatter(df, x='Probabilidad', y='Impacto', color='Profesión', title='Probabilidad vs Impacto')
    st.plotly_chart(fig_prob_impacto)

    st.header("Distribución de Profesiones")
    fig_profesiones = px.pie(df, names='Profesión', title='Distribución de Profesiones')
    st.plotly_chart(fig_profesiones)

    st.header("Riesgo por Profesión")
    fig_riesgo_profesion = px.bar(df, x='Profesión', y='Riesgo', color='Riesgo', title='Riesgo por Profesión')
    st.plotly_chart(fig_riesgo_profesion)