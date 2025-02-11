
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import pandas as pd


@st.cache_data
def load_data():
    file_path = "df_new_3.csv"  # Substitua pelo caminho correto
    try:
        df = pd.read_csv(file_path)
        df["Creation Date"] = pd.to_datetime(
            df["Creation Date"], errors='coerce')
        return df
    except FileNotFoundError:
        st.error("Erro: Arquivo df_new_3.csv não encontrado!")
        return pd.DataFrame()  # Retorna um DataFrame vazio para evitar erros


df = load_data()
