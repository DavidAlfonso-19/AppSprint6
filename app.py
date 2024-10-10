import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Proyecto 6')
st.write('Marque la casilla de el diagrama que desea crear')

hist_checkbox = st.checkbox('Construir histograma') # crear un botón       
if hist_checkbox: # al hacer clic en el checkbox
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
scatter_checkbox= st.checkbox('contruir un scatter')
if scatter_checkbox: # al hacer clic en el checkbox
    # escribir un mensaje
    st.write('Creación de un scatter para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y= 'price')
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)