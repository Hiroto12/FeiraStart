import streamlit as st
from datetime import date
import pandas as pd
from PIL import Image
import datetime
import numpy as np

from plotly import graph_objs as go

import plotly.express as px

st.title("Sumá Tech ")
data_fim = date.today().strftime('%Y-%m-%d')

st.sidebar.header('Protótipo Sumá Tech')

acao = st.sidebar.radio('Selecione a página', ('Pesquisa de Lotes disponíveis','Monitoramento dos Lotes'))
# acao = 'Previsão de Volume'

combustiveis = ['Una', 'Pacas', 'Centro']
opcoes = ['Lugar X', 'Lugar Y']
metas = ['Meta de Nº Abastecimento', 'Meta de Comparação', 'Meta de Tanque Cheio', 'Meta de Fidelidade']


def pegar_dados():
    return pd.read_csv(r'C:\Users\hirot\arima_comum_total_total6.csv')

def pegar_previsao():
    return pd.read_csv(r'C:\Users\hirot\gmax\previsa_'+f'{nome_acao}'+'.csv')

def pegar_meta_abastecimento():
    return pd.read_csv(r'C:\Users\hirot\meta_abastecimento_total.csv')

def pegar_meta_comparacao_comum():
    return pd.read_csv(r'C:\Users\hirot\meta_comparacao_comum.csv')

def pegar_meta_comparacao_aditivada():
    return pd.read_csv(r'C:\Users\hirot\meta_comparacao_aditivada.csv')

def pegar_meta_comparacao_dif():
    return pd.read_csv(r'C:\Users\hirot\meta_comparacao_dif.csv')

##--
def pegar_previsao_comum():
    return pd.read_csv(r'C:\Users\hirot\previsa_Gasolina Comum.csv')
##---
def pegar_alocar():
    return pd.read_csv(r'C:\Users\hirot\alocar3.csv')

def convert_df(df):
   return df.to_csv().encode('utf-8')

def pegar_nfidelizados():
    return pd.read_csv(r'C:\Users\hirot\previsao_nfidelizados.csv')

if (acao == 'Monitoramento dos Lotes'):
    st.warning('Programa está em protótipo. Todos os dados são meramente ilustrativos')



    nome_acao = st.selectbox('Lotes monitorados:', opcoes)

    if (nome_acao == 'Lugar X'):
        col1, col2 = st.columns(2)
        with col1:

            image = Image.open(r'C:\Users\hirot\Pictures\lotes_start\lote1.jpg')
            st.image(image, caption='Terreno localizado em pasárgada', width=300)

        with col2:
            st.info('Tamanho do Lote: 1000m²')
            st.info('Ponto de água próximo')
            st.info('Área Rural')

        col1, col2 = st.columns(2)

        with col1:
            st.write('Gráfico de Produção de Hortaliças')
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['Couve', 'Alface', 'Almeirão'])

            st.line_chart(chart_data)

        with col2:
            st.write('Gráfico de Produção de Grãos')
            chart_data = pd.DataFrame(
                np.random.randn(50, 3),
                columns=['Milho', 'Soja', 'Girassol'])

            st.line_chart(chart_data)






        d = st.date_input(
            "Data da Produção",
            datetime.date(2022, 7, 1))
        aux = d

        st.write("Produções de hortaliças")
        number = st.number_input('Quantidade de Couve: ', step=1)
        number2 = st.number_input('Quantidade de Almeirão: ', step=1)
        number3 = st.number_input('Quantidade de Alface: ', step=1)

        st.write("Produções de Grãos")
        number4 = st.number_input('Kg de Milho: ')
        number5 = st.number_input('Kg de Soja: ')
        number6 = st.number_input('Kg de Girassol:')

    if (nome_acao == 'Lugar Y'):
        col1, col2 = st.columns(2)
        with col1:

            image = Image.open(r'C:\Users\hirot\Pictures\lotes_start\lote2.jpg')
            st.image(image, caption='Terreno localizado em pasárgada', width=300)

        with col2:
            st.info('Tamanho do Lote: 1000m²')
            st.info('Ponto de água próximo')
            st.info('Área Rural')

        col1, col2 = st.columns(2)

        with col1:
            st.write('Gráfico de Produção de Hortaliças')
            chart_data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['Couve', 'Alface', 'Almeirão'])

            st.line_chart(chart_data)

        with col2:
            st.write('Gráfico de Produção de Grãos')
            chart_data = pd.DataFrame(
                np.random.randn(50, 3),
                columns=['Milho', 'Soja', 'Girassol'])

            st.line_chart(chart_data)






        d = st.date_input(
            "Data da Produção",
            datetime.date(2022, 7, 1))
        aux = d

        st.write("Produções de hortaliças")
        number = st.number_input('Quantidade de Couve: ', step=1)
        number2 = st.number_input('Quantidade de Almeirão: ', step=1)
        number3 = st.number_input('Quantidade de Alface: ', step=1)

        st.write("Produções de Grãos")
        number4 = st.number_input('Kg de Milho: ')
        number5 = st.number_input('Kg de Soja: ')
        number6 = st.number_input('Kg de Girassol:')


if (acao == 'Pesquisa de Lotes disponíveis'):

    st.warning('Programa está em protótipo. Todos os dados são meramente ilustrativos')

    st.subheader('Locais com lotes disponíveis')

    df = pd.DataFrame(
        np.random.randn(50, 2) / [25, 25] + [-19.8252042, -43.362126],
        columns=['lat', 'lon'])

    st.map(df)

    nome_acao = st.selectbox('Lotes disponíveis:', combustiveis)
    df = pegar_dados()

    if (nome_acao == 'Una'):

        col1, col2 = st.columns(2)
        with col1:

            image = Image.open(r'C:\Users\hirot\Pictures\lotes_start\lote1.jpg')
            st.image(image, caption='Lote localizado em XXXYYYZZZ', width=300)

        with col2:
            st.info('Tamanho do Lote: 1000m²')
            st.info('Ponto de água próximo')
            st.info('Área Rural')


    if (nome_acao == 'Pacas'):

        col1, col2 = st.columns(2)
        with col1:
            image = Image.open(r'C:\Users\hirot\Pictures\lotes_start\lote2.jpg')
            st.image(image, caption='Lote localizado em XXXYYYZZZ', width=350)

        with col2:
            st.info('Tamanho do Lote: 1000m²')
            st.info('Ponto de água próximo')
            st.info('Área Rural')

    if (nome_acao == 'Centro'):

        col1, col2 = st.columns(2)
        with col1:
            image = Image.open(r'C:\Users\hirot\Pictures\lotes_start\lote3.jpg')
            st.image(image, caption='Lote localizado em XXXYYYZZZ', width=350)

        with col2:
            st.info('Tamanho do Lote: 1000m²')
            st.info('Ponto de água próximo')
            st.info('Área Urbana')











if(acao == 'Gestão de Metas'):
    nome_acao2 = st.selectbox('Gestão Inteligente de Metas', metas)
    n_dias_meta = st.slider('Quantidade de dias de previsão', 10, 70)

    if (nome_acao2 == 'Meta de Nº Abastecimento'):
        df_meta = pegar_meta_abastecimento()
        st.subheader(f'Tabela de Previsão - {nome_acao2}')
        st.write(df_meta.head(n_dias_meta))

        numeroturno1 = st.number_input('Insere a quantidade de Frentista - Turno da Manhã', min_value=1,step=1)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Diariamente")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Manha']/numeroturno1)
            st.write(aux1[['Data','Média por Frentista']])

        with col2:
            st.subheader("Média durante a previsão")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Manha'] / numeroturno1)
            st.write('Valor Médio de Abastecimento:',round(aux1['Média por Frentista'].mean()))
            with st.container():
                fig = px.line(aux1, x=aux1.Data, y=aux1['Média por Frentista'], width=400, height=400)
                st.plotly_chart(fig)




        numeroturno2 = st.number_input('Insere a quantidade de Frentista - Turno da Tarde', min_value=1,step=1)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Diariamente")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Tarde'] / numeroturno2)
            st.write(aux1[['Data', 'Média por Frentista']])

        with col2:
            st.subheader("Média durante a previsão")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Tarde'] / numeroturno2)
            st.write('Valor Médio de Abastecimento:', round(aux1['Média por Frentista'].mean()))
            with st.container():
                fig = px.line(aux1, x=aux1.Data, y=aux1['Média por Frentista'], width=400, height=400)
                st.plotly_chart(fig)

        numeroturno3 = st.number_input('Insere a quantidade de Frentista - Turno da Noite', min_value=1,step=1)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Diariamente")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Noite'] / numeroturno2)
            st.write(aux1[['Data', 'Média por Frentista']])

        with col2:
            st.subheader("Média durante a previsão")
            aux1 = df_meta
            aux1['Média por Frentista'] = (aux1['Turno Noite'] / numeroturno3)
            st.write('Valor Médio de Abastecimento:', round(aux1['Média por Frentista'].mean()))
            with st.container():
                fig = px.line(aux1, x=aux1.Data, y=aux1['Média por Frentista'], width=400, height=400)
                st.plotly_chart(fig)

    if (nome_acao2 == 'Meta de Comparação'):

        df_meta = pegar_meta_comparacao_comum()
        df_meta2 = pegar_meta_comparacao_aditivada()

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gasolina Comum")
            aux1 = df_meta
            st.write(aux1.head(n_dias_meta))


        with col2:
            st.subheader("Gasolina Aditivada")
            aux1 = df_meta2
            st.write(aux1.head(n_dias_meta))

        col1, col2 = st.columns(2)
        with col1:
            df_meta3 = pegar_meta_comparacao_dif()
            numeroturno1 = st.number_input('Insere a quantidade de Frentista - Turno da Manha', min_value=1, step=1)
            conta = (((df_meta3[['Turno Manha G.Aditivada']].values)) / ((df_meta3[['Turno Manha G.Comum']].values))) / numeroturno1
            df_meta3['Comparação'] = conta
            st.write(df_meta3[['Data','Turno Manha G.Comum','Turno Manha G.Aditivada', 'Comparação']])
        with col2:
            mean1= (df_meta3[['Comparação']].values).mean()
            st.write('Média durante o intervalo da previsão:',mean1)

        # n_dias_meta = st.slider('Quantidade de dias que ', 1, 79)
        # auxiliar_somatoria = df_meta3.head(n_dias_meta)
        # somatoria = (auxiliar_somatoria[['Comparação']].values).sum()
        # st.write('Valor da Comparação:', somatoria)
        col1, col2 = st.columns(2)

        with col1:
            numeroturno2 = st.number_input('Insere a quantidade de Frentista - Turno da Tarde', min_value=1, step=1)
            conta = (((df_meta3[['Turno Tarde G.Aditivada']].values)) / (
            (df_meta3[['Turno Tarde G.Comum']].values))) / numeroturno2
            df_meta3['Comparação'] = conta
            st.write(df_meta3[['Data', 'Turno Tarde G.Comum', 'Turno Tarde G.Aditivada', 'Comparação']])
        with col2:
            mean1= (df_meta3[['Comparação']].values).mean()
            st.write('Média durante o intervalo da previsão:',mean1)

        # n_dias_meta2 = st.slider('Quantidade de dias  ', 1, 79)
        # auxiliar_somatoria = df_meta3.head(n_dias_meta2)
        # somatoria = (auxiliar_somatoria[['Comparação']].values).sum()
        # st.write('Valor da Comparação:', somatoria)

        col1, col2 = st.columns(2)

        with col1:
            numeroturno3 = st.number_input('Insere a quantidade de Frentista - Turno da Noite', min_value=1, step=1)
            conta = (((df_meta3[['Turno Noite G.Aditivada']].values)) / (
            (df_meta3[['Turno Noite G.Comum']].values))) / numeroturno3
            df_meta3['Comparação'] = conta
            st.write(df_meta3[['Data', 'Turno Noite G.Comum', 'Turno Noite G.Aditivada', 'Comparação']])

        with col2:
            mean1= (df_meta3[['Comparação']].values).mean()
            st.write('Média durante o intervalo da previsão:',mean1)


        # n_dias_meta3 = st.slider('Quantidade de dias ', 1, 79)
        # auxiliar_somatoria = df_meta3.head(n_dias_meta3)
        # somatoria = (auxiliar_somatoria[['Comparação']].values).sum()
        # st.write('Valor da Comparação:', somatoria)

    if(nome_acao2 == 'Meta de Tanque Cheio'):
        df_meta3 = pegar_previsao_comum()
        df_meta = pegar_meta_comparacao_comum()

        df_meta3 = df_meta3[1:]

        df_meta3 = df_meta3.head(84)
        df_meta = df_meta.head(84)

        df_meta3['Turno Manha'] = (df_meta3[['Previsão']].values)/0.49
        df_meta3['Turno Tarde'] = (df_meta3[['Previsão']].values) / 0.41
        df_meta3['Turno Noite'] = (df_meta3[['Previsão']].values) / 0.10

        df_meta_comum = df_meta3[['Data', 'Turno Manha', 'Turno Tarde', 'Turno Noite']]

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Nº de abastecimento de Gasolina Comum")
            aux1 = df_meta
            st.write(aux1)

        with col2:
            st.subheader("Quantidade de Volume de Gasolina Comum")
            aux2 = df_meta_comum
            st.write(aux2)

        df_media_meta = df_meta3[['Data']]
        df_media_meta['Média da Manha'] = ((df_meta_comum[['Turno Manha']].values)/(df_meta[['Turno Manha']].values))
        df_media_meta['Média da Tarde'] = ((df_meta_comum[['Turno Tarde']].values) / (df_meta[['Turno Tarde']].values))
        df_media_meta['Média da Noite'] = ((df_meta_comum[['Turno Noite']].values) / (df_meta[['Turno Noite']].values))

        st.write("Média de litro por abastecimento por dia:")
        st.write(df_media_meta)

        col1, col2 = st.columns (2)

        with col1:
            numeroturno3 = st.number_input('Insere a quantidade de Frentista - Turno da Manha', min_value=1, step=1)
            conta = ((df_media_meta[['Média da Manha']].values)/ numeroturno3)
            df_meta3['Média por Frentista'] = conta
            st.write(df_meta3[['Data', 'Média por Frentista']])

        with col2:
            mean1= (df_meta3[['Média por Frentista']].values).mean()
            st.write('Média por frentista durante o intervalo da previsão:',mean1)

        col1, col2 = st.columns(2)

        with col1:
            numeroturno3 = st.number_input('Insere a quantidade de Frentista - Turno da Tarde', min_value=1, step=1)
            conta = ((df_media_meta[['Média da Tarde']].values) / numeroturno3)
            df_meta3['Média por Frentista'] = conta
            st.write(df_meta3[['Data', 'Média por Frentista']])

        with col2:
            mean1 = (df_meta3[['Média por Frentista']].values).mean()
            st.write('Média por frentista durante o intervalo da previsão:', mean1)


        col1, col2 = st.columns(2)

        with col1:
            numeroturno3 = st.number_input('Insere a quantidade de Frentista - Turno da Noite', min_value=1, step=1)
            conta = ((df_media_meta[['Média da Noite']].values) / numeroturno3)
            df_meta3['Média por Frentista'] = conta
            st.write(df_meta3[['Data', 'Média por Frentista']])

        with col2:
            mean1 = (df_meta3[['Média por Frentista']].values).mean()
            st.write('Média por frentista durante o intervalo da previsão:', mean1)


    if (nome_acao2 == 'Meta de Fidelidade'):
        df = pegar_nfidelizados()
        df['Previsao'] = df[['Nº de abastecimento']]

        st.write('Previsão dos Números de Abastecimentos dos Não Fidelizados')

        df_previsao = df.head(n_dias_meta)
        df_previsao = df_previsao[['Data', 'Previsao']]

        col1, col2 = st.columns(2)

        with col1:
            st.write(df_previsao)

        with col2:
            fig = px.line(df_previsao, x=df_previsao.Data, y=df_previsao.Previsao, width=400, height=400)
            st.plotly_chart(fig)










        # st.write('Valor Médio de Abastecimento:',round(aux1['Média por Frentista'].mean()))

def calcular_peso(options, nome):
    indice = options.index(nome)

    if (indice == 0):
        return 5
    if (indice == 1):
        return 4
    if (indice == 2):
        return 3
    if (indice == 3):
        return 2



if (acao == 'Alocação de Frentista'):
    options = st.multiselect(
        'Ordem de prioridade das Metas',
        ['Meta de Abastecimento', 'Meta de Comparação', 'Meta de Tanque Cheio', 'Meta de Fidelidade'])

    if (len(options)!=4):
        st.write("Insere todos os elementos conforme a ordem de prioridade")
    if (len(options) == 4):
        peso_ab = calcular_peso(options, 'Meta de Abastecimento')
        peso_co = calcular_peso(options, 'Meta de Comparação')
        peso_tc = calcular_peso(options, 'Meta de Tanque Cheio')
        peso_fd = calcular_peso(options, 'Meta de Fidelidade')

        df = pegar_alocar()
        df['Média Ponderada'] = (((df[['Abastecimento_Batido']].values) * peso_ab) + (
                    (df[['Comparacao_Batida']].values) * peso_co) +
                                 ((df[['Tanque_Batido']].values) * peso_tc) + (
                                             (df[['Fidelidade_Batido']].values) * peso_fd)) / 14


        st.write('Tabela dos frentista com melhor pontuação ', df.sort_values(by='Média Ponderada', ascending=False))

        st.write('T ')




#‪C:\Users\hirot\Music\previsao.png
# pkl_path = "C:/Users/hirot/Prophet.pkl"
# with open(pkl_path, 'rb') as f:
#     m = pickle.load(f)
#
# grafico1 = plot_plotly(m, previsao)
# st.plotly_chart(grafico1)
#
# grafico2 = plot_components_plotly(modelo, previsao)
# st.plotly_chart(grafico2)

