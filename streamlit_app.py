import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Aplicación Interactiva de Ciencia de Datos")

# Descripción de la aplicación
st.write("""
Esta aplicación permite cargar un archivo CSV, visualizar los datos, 
y realizar un análisis exploratorio con gráficos.
""")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Cargar datos
    df = pd.read_csv(uploaded_file)
    
    # Mostrar el dataframe
    st.subheader("Datos del archivo:")
    st.dataframe(df)
    
    # Mostrar estadísticas descriptivas
    st.subheader("Estadísticas descriptivas:")
    st.write(df.describe())
    
    # Seleccionar columnas para visualizar gráficos
    st.subheader("Gráficos interactivos")
    columnas = df.columns.tolist()
    
    # Gráfico de dispersión
    st.write("Gráfico de dispersión:")
    col_x = st.selectbox("Selecciona columna para el eje X", columnas)
    col_y = st.selectbox("Selecciona columna para el eje Y", columnas)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax)
    st.pyplot(fig)

    # Gráfico de barras
    st.write("Gráfico de barras:")
    col_bar = st.selectbox("Selecciona una columna para el gráfico de barras", columnas)
    
    fig, ax = plt.subplots()
    df[col_bar].value_counts().plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Matriz de correlación
    st.write("Matriz de correlación:")
    if st.checkbox("Mostrar matriz de correlación"):
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
else:
    st.write("Sube un archivo CSV para comenzar.")

