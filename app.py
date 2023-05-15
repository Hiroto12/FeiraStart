import streamlit as st
import pandas as pd
import numpy as np

df2 = pd.read_csv(r'C:\Users\hirot\dados_teste_lingo.csv')


def main():
    st.title('Análise de Progresso dos Alunos')
    st.sidebar.header('Filtro')
    # Filtro para Nome Completo
    selected_name = st.sidebar.text_input('Nome completo')

    # Filtro para Resultado de Nivelamento
    unique_results = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    selected_result = st.sidebar.multiselect('Resultado nivelamento', unique_results, unique_results)

    # Filtro para Leva
    unique_levas = df2['Leva'].unique()
    selected_leva = st.sidebar.multiselect('Leva', unique_levas, unique_levas)

    # Filtro para Área
    unique_areas = df2[df2['Área'] != '-']['Área'].unique()
    selected_area = st.sidebar.multiselect('Área', unique_areas, unique_areas)

    df_selected = df2.copy()

    # Excluir a coluna "Unnamed: 0"
    df_selected.drop('Unnamed: 0', axis=1, inplace=True)

    if selected_name:
        df_selected = df_selected[df_selected['Nome completo'].str.contains(selected_name)]

    df_selected = df_selected[df_selected['Resultado nivelamento'].isin(selected_result)]
    df_selected = df_selected[df_selected['Leva'].isin(selected_leva)]
    df_selected = df_selected[df_selected['Área'].isin(selected_area)]

    st.write(df_selected)

    # Distribuição de alunos por nível
    st.subheader('Distribuição de alunos por nível')
    level_counts = df_selected['Resultado nivelamento'].value_counts()
    st.bar_chart(level_counts)

    # Tempo gasto na plataforma e AoV
    st.subheader('Tempo gasto na plataforma e AoV')
    time_data = pd.DataFrame(df_selected[['tempo plataforma minutos', 'tempo AOV minutos']])
    st.line_chart(time_data)
    
main()
