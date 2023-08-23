import streamlit as st

from typing import Callable


def series_tiempo_sidebar() -> str:
    """
    Display the sidebar for selecting the virus type.

    Returns:
        str: The selected virus type.
    """
    virus_filter_can_end = st.selectbox('Seleccione el virus:', options=["", 'Dengue', 'Zika', 'Chikungunya'])
    return virus_filter_can_end


def series_tiempo_info_general():
    """
    Display general information about time series analysis.
    """
    st.markdown('Una serie de tiempo es un conjunto de observaciones secuenciales registradas a lo largo del tiempo, donde cada punto de datos refleja el valor de una variable en momentos específicos. Estas series son ampliamente utilizadas en análisis estadísticos para comprender y predecir patrones de comportamiento en función de la temporalidad.')
    st.markdown('En el contexto del modelado y predicción de casos de dengue, la importancia radica en la capacidad de analizar la evolución histórica de la enfermedad a lo largo de distintos períodos, lo que permite identificar tendencias, estacionalidades y ciclos recurrentes.')
    st.markdown('El modelado y la predicción de casos de dengue no solo brindan una comprensión más profunda de los factores subyacentes que afectan la propagación de la enfermedad, sino que también tienen un valor crucial para la salud pública al proporcionar a los responsables de la toma de decisiones herramientas para anticipar y mitigar brotes, asignar recursos eficazmente y planificar estrategias de prevención y control con mayor precisión.')


def series_tiempo_info_tablero():
    """
    Display information about the time series analysis dashboard.
    """
    st.markdown('En el tablero colaborativo se ha realizado un análisis serie temporal para una comprensión completa de la evolución de los casos de dengue en el período comprendido entre 2007 y 2023. ')
    st.markdown('Este análisis se enfoca en aspectos esenciales del análisis y la predicción de la serie de tiempo, lo que resulta fundamental para gestionar eficazmente la propagación de esta enfermedad.')
    st.markdown('El primer análisis muestra la descomposición detallada de la serie de tiempo de casos de dengue. A través de esta descomposición, se logra una clara identificación de patrones de tendencia y estacionalidad, brindando una comprensión profunda de cómo ha evolucionado la propagación de la enfermedad con el tiempo. Este análisis destaca los cambios de largo plazo y permite reconocer tendencias significativas.')
    st.markdown('El siguiente es un análisis de los residuales de la serie de tiempo. Estos residuales ofrecen una perspectiva adicional al revelar patrones que podrían haber escapado a la descomposición. Este análisis es esencial para detectar eventos anómalos o cambios inusuales en la propagación de los casos de dengue, lo que ayuda a adaptar las estrategias de prevención y control en tiempo real.')
    st.markdown('Por último, la tercera hoja del tablero colaborativo despliega una herramienta de predicción vital. Los filtros que se aplican según el departamento, municipio y año permiten proyectar escenarios futuros de casos de dengue. Esto se traduce en una toma de decisiones informada, permitiendo la planificación precisa de recursos y estrategias para abordar posibles brotes de la enfermedad.')


def series_tiempo(virus_filter_can_end: str, CONF: dict, open_link: Callable, show_link: Callable):
    """
    Display information about time series analysis based on the selected virus type.

    Args:
        virus_filter_can_end (str): The selected virus type.
        CONF (dict): Configuration data.
        open_link (function): A function to open a link.
        show_link (function): A function to show a link.
    """
    if virus_filter_can_end == 'Dengue':

        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter_can_end}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter_can_end.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter_can_end}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter_can_end.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')
        
        st.markdown('-----')
        st.markdown('##### En el siguiente enlace puedes consultar los canales endémicos asociados y explorar las representaciones gráficas de la incidencia de diversas enfermedades.')
        series_tiempo_info_tablero()
        open_link(CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()], f'Series de Tiempo para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()])

    elif virus_filter_can_end == 'Zika':

        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter_can_end}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter_can_end.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter_can_end}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter_can_end.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')
        
        st.markdown('-----')
        st.markdown('##### En el siguiente enlace puedes consultar los canales endémicos asociados y explorar las representaciones gráficas de la incidencia de diversas enfermedades.')
        series_tiempo_info_tablero()
        open_link(CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()], f'Series de Tiempo para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()])

    elif virus_filter_can_end == 'Chikungunya':

        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter_can_end}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter_can_end.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter_can_end}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter_can_end.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')
        
        st.markdown('-----')
        st.markdown('##### En el siguiente enlace puedes consultar los canales endémicos asociados y explorar las representaciones gráficas de la incidencia de diversas enfermedades.')
        series_tiempo_info_tablero()
        open_link(CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()], f'Series de Tiempo para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['SERIES_TIEMPO'][virus_filter_can_end.upper()])
    
    else:

        series_tiempo_info_general()
        st.markdown('-----')
        st.markdown('### :arrow_left: Por favor seleccione una de las enfermedades en el panel izquierdo para visualizar la información')
        st.markdown('##### Este portal posee información clasificada de la siguiente manera:')
        st.markdown('- Dengue')
        st.markdown('- Zika')
        st.markdown('- Chikungunya')
        st.markdown('-----')
        st.markdown('Al seleccionar uno de los virus específicos, tendrás acceso a información detallada sobre los canales endémicos asociados.')
