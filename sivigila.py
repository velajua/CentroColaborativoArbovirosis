import streamlit as st

from typing import Callable


def sivigila_sidebar(CONF: dict, open_link: Callable):
    """
    Display the Sivigila sidebar links.

    Args:
        CONF (dict): Configuration dictionary.
        open_link (callable): Function to open a link.
    """
    st.markdown('-----')
    open_link(CONF['LINIAMIENTOS'], f'Liniamientos')
    open_link(CONF['PUBLICACIONES'], f'Publicaciones')
    open_link(CONF['DICCIONARIO_DATOS'], f'Diccionario de Datos')


def sivigila(CONF: dict, open_link: Callable):
    """
    Display Sivigila information.

    Args:
        CONF (dict): Configuration dictionary.
        open_link (callable): Function to open a link.
    """
    st.markdown('# Sivigila - INS')
    
    st.markdown('##### En el siguiente enlace encontrarás información detallada sobre diversos aspectos relacionados con la pandemia de COVID-19 y otros temas de salud.')
    st.markdown('##### Algunas de las cosas que puedes encontrar incluyen:')
    col_ins_1, col_ins_2 = st.columns([1, 1])
    with col_ins_1:
        st.markdown('''
- El Reporte COVID
  - Que proporciona datos actualizados sobre la situación epidemiológica
- El Reporte COVID-19
  - Que presenta estadísticas específicas sobre la enfermedad
- Los Indicadores COVID-19
  - Que ofrecen métricas y tendencias relacionadas con el virus
- Comportamientos Inusuales
  - Que examina patrones atípicos de la enfermedad
- Enfermedades no transmisibles y transmisibles
  - Que exploran diferentes enfermedades y su propagación
''')
    with col_ins_2:
        st.markdown('''
- Eventos de factores de riesgo ambiental y sanitario
  - Que analiza situaciones que pueden aumentar la probabilidad de contagio
- Salud mental y lesiones de causa externa
  - Que aborda aspectos psicológicos y lesiones accidentales
- Incidencias
  - Que registra casos y eventos específicos
- Poblaciones especiales
  - Que se centra en grupos vulnerables o particulares
- Indicadores de desempeño
  - Que evalúan la eficacia de las medidas implementadas''')

    open_link(CONF['SIVIGILA'], 'Portal Sivigila INS')
    
    st.markdown('-----')
    st.markdown('##### En el siguiente enlace encontrarás más información acerca de los boletines epidemiologicos semanales.')
    open_link(CONF['BOLETIN_EPIDEMIOLOGICO'], 'Boletín Epidemiológico')
