import pandas as pd
import streamlit as st
import plotly.express as px


df_car_data = pd.read_csv('vehicles.csv')

st.header('Sprint 5')
st.header('Desenvolvendo Aplicativo Web')
st.write('Projeto desenvolvido para conclusão da Sprint 5')
st.write('Neste projeto estamos utilizando um conjunto de dados que reúne anúncios de vendas de carros. Para criar os gráficos abaixo, você pode selecionar as colunas que desejar.')


column_options = df_car_data.columns.tolist()


st.title('Histograma')
selected_column_hist = st.selectbox(
    'Selecione a coluna para o histograma:', column_options, key='hist')

hist_checkbox = st.checkbox('Criar histograma')

if hist_checkbox:
    message_placeholder = st.empty()
    message_placeholder.text('Histograma sendo criado. Aguarde...')

    fig_hist = px.histogram(df_car_data, x=selected_column_hist)
    st.plotly_chart(fig_hist, use_container_width=True)

    message_placeholder.text('Histograma criado com sucesso')


st.title('Gráfico de Dispersão')
x_column = st.selectbox(
    'Selecione a coluna X para o gráfico de dispersão:', column_options, key='scatter_x')
y_column = st.selectbox(
    'Selecione a coluna Y para o gráfico de dispersão:', column_options, key='scatter_y')


scatter_checkbox = st.checkbox('Criar gráfico de dispersão')

if scatter_checkbox:
    message_placeholder = st.empty()
    message_placeholder.text('Gráfico sendo criado. Aguarde...')

    fig_scatter = px.scatter(df_car_data, x=x_column, y=y_column)
    st.plotly_chart(fig_scatter, use_container_width=True)

    message_placeholder.text('Gráfico criado com sucesso')
