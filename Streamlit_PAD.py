# =================================================================
# == INSTITUTO TECNOLOGICO Y DE ESTUDIOS SUPERIORES DE OCCIDENTE ==
# ==          ITESO, UNIVERSIDAD JESUITA DE GUADALAJARA          ==
# ==                                                             ==
# ==             MAESTRÍA EN SISTEMAS COMPUTACIONALES            ==
# ==              PROGRAMACIÓN PARA ANÁLISIS DE DATOS            ==
# ==                  IMPLEMENTACIÓN EN STREAMLIT                ==
# =================================================================

#Importación de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from skimage import io

#Lectura de los datos de los Administradores desde el archivo CSV
datos_df = pd.read_csv('./Datos/Datos_DF.csv')

#Lectura de la Imagen
Logo = io.imread("./Imagenes/ITESO_Logo.png")

#Renderizado de la imagen
st.image(Logo, width = 500)

#Renderizado del texto
st.title("Uso Básico de Streamlit")
st.subheader(":blue[Streamlit es un *framework* para la creación de aplicaciones web interactivas y basadas en datos.]")

#Renderizado del texto
st.markdown("**Manejo de Información de Clientes**")
st.markdown(":blue[Este **DataFrame** contiene información de varias personas, las ciudades donde viven, así como sus ganancias a lo largo de un año.]")

#Renderizado del DataFrame
st.dataframe(datos_df)

#Renderizado de la Imagen y el Título en el Dashboard
st.sidebar.image(Logo, width = 200)
st.sidebar.markdown("## CONFIGURACIÓN")

#Selector del Mes en el Dashboard
vars_mes = ['ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']
default_hist = vars_mes.index('ENE')
histo_selected = st.sidebar.selectbox('Mes para el Histograma:', vars_mes, index = default_hist)

#Selector de las Personas en el Dashboard
vars_per = ['Iñaki González','María Cázares','José García','Jérémie Muñoz','Agnès Villalón','Bérénice Pitkämäki','Geneviève Rukajärvi','Hélène Ñuñoz','Ñaguí Grönholm','Iván Földváry']
default_pers = vars_per.index('Iñaki González')
ganan_selected = st.sidebar.selectbox('Ganancias Personales:', vars_per, index = default_pers)

#Selector del Mapa de Color en el Dashboard
vars_cmap = ['crest', 'viridis', 'OrRd','Pastel1', 'Paired', 'ocean', 'jet', 'Accent','Dark2','twilight']
default_cmap = vars_cmap.index('crest')
color_selected = st.sidebar.selectbox('Color de la Matriz de Correlación:', vars_cmap, index = default_cmap)

#Selector de los Meses para el Histograma en el Dashboard
mes_multi_selected = st.sidebar.multiselect('Elementos de la Matriz de Correlación:', vars_mes, default = vars_mes)

#Definición de las columnas
colum_izq, colum_der = st.columns(2)

#Título para el gráfico
colum_izq.subheader('Histograma')

#Inicialización del gráfico
fig1, ax1 = plt.subplots()

#Generación del gráfico
sns.set(style = "darkgrid")
sns.histplot(data = datos_df[histo_selected])
ax1.set_title('Histograma de Valores')
ax1.set_xlabel(histo_selected)
ax1.set_ylabel('Frecuencia')

#Renderización del gráfico
colum_izq.pyplot(fig1)

#Título para el gráfico
colum_der.subheader('Ganancias')

#Inicialización del gráfico
fig2, ax2 = plt.subplots()

#Generación del gráfico
if ganan_selected == 'Iñaki González':
    periodo_df = datos_df.iloc[0]
elif ganan_selected == 'María Cázares':
    periodo_df = datos_df.iloc[1]
elif ganan_selected == 'José García':
    periodo_df = datos_df.iloc[2]
elif ganan_selected == 'Jérémie Muñoz':
    periodo_df = datos_df.iloc[3]
elif ganan_selected == 'Agnès Villalón':
    periodo_df = datos_df.iloc[4]
elif ganan_selected == 'Bérénice Pitkämäki':
    periodo_df = datos_df.iloc[5]
elif ganan_selected == 'Geneviève Rukajärvi':
    periodo_df = datos_df.iloc[6]
elif ganan_selected == 'Hélène Ñuñoz':
    periodo_df = datos_df.iloc[7]
elif ganan_selected == 'Ñaguí Grönholm':
    periodo_df = datos_df.iloc[8]
elif ganan_selected == 'Iván Földváry':
    periodo_df = datos_df.iloc[9]
else:
    periodo_df = datos_df
periodo_df = periodo_df.transpose()
periodo_df = periodo_df.to_frame()
periodo_df = periodo_df.rename(columns = {1: 'MES'})
periodo_df = periodo_df.drop(['NOMBRE','APELLIDO','CIUDAD'])
plt.plot(periodo_df)
ax2.set_title('Ganancias Mensuales por Persona')
ax2.set_xlabel(ganan_selected)
ax2.set_ylabel('Ganancias')

#Renderización del gráfico
colum_der.pyplot(fig2)

#Título para el gráfico
st.subheader('Matriz de Correlación')

#Inicialización del gráfico
fig3, ax3 = plt.subplots()

#Generación del gráfico
df_corr = datos_df[mes_multi_selected].corr()
sns.heatmap(df_corr, annot = True, fmt='.2f', cmap = color_selected)

#Renderización del gráfico
st.pyplot(fig3)