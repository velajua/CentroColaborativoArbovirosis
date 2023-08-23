import streamlit as st

# from st_clickable_images import clickable_images
from typing import Callable


def canales_endemicos_info_general():
    """
    Display general information about endemic channels.
    """
    st.markdown('''Un canal endémico es una herramienta que proporciona información sobre la prevalencia y distribución de una enfermedad en un período de estudio determinado.
                Este canal permite a los profesionales de la salud identificar patrones y tendencias al ofrecer datos sobre la frecuencia esperada de casos del evento.
                Su principal utilidad radica en su capacidad para predecir y controlar brotes de enfermedades, ya que establece una línea de base que permite evaluar si los casos se encuentran dentro de los límites normales o si hay un aumento o disminución significativa que requiere intervención.
                Además, el canal endémico puede detectar cambios estacionales, factores de riesgo y evaluar la efectividad de las estrategias de control implementadas.''')


def canales_endemicos_info_tablero():
    """
    Display information about the endemic channels dashboard.
    """
    st.markdown('''El tablero a continuación muestra el canal endémico para el evento de Dengue mediante la metodología de Medias y Medianas y la metodología de Bortman.
                El tablero permite filtrar por Departamento, Municipio, Grupo de Edad y seleccionar los años con los cuales se desea realizar la evaluación histórica del evento.
                Para ambas metodologías se establecieron los siguientes limites: comportamiento por debajo de lo esperado (por debajo del limite inferior del Intervalo de confianza al 95 % para el caso de Bortman o por debajo del percentil 25 para el caso de medianas);
                dentro de lo esperado (entre el limite inferior del Intervalo de confianza al 95 % y entre el percentil 25 y la media geométrica para el caso de medianas), en alerta (entre la media geométrica y el limite superior del intervalo de confianza al 95 % para Bortman y entre la mediana y el percentil 75 ):
                por encima de lo esperado (superior al limite superior del intervalo de confianza al 95 % para el caso de Bortman y por encima del percentil 75 para el caso de medianas).''')

    
# def load_image(virus_filter_can_end, ):
#     title_, cat_, empty_ = st.columns([10, 1, 10])
#     with title_:
#         st.markdown(f'# Canales Endémicos{" - " if virus_filter_can_end else ""}{virus_filter_can_end}')
#     with cat_:
#         imgs_ = clickable_images(['https://gaenvironmentalgroup.com/wp-content/uploads/2016/03/blank-50x50.png'])
#         if imgs_ > -1:
#             imgs_ = -1
#             image_url = "https://freepngimg.com/thumb/categories/96.png"
#             st.image(image_url)


def canales_endemicos_sidebar() -> str:
    """
    Create the sidebar for selecting the virus type.

    Returns:
        str: The selected virus type.
    """
    virus_filter_can_end = st.selectbox('Seleccione el virus:', options=["", 'Dengue', 'Zika', 'Chikungunya'])
    return virus_filter_can_end


def canales_endemicos(virus_filter_can_end: str, CONF: dict, open_link: Callable, show_link: Callable):
    """
    Display information about endemic channels based on the selected virus type.

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
        canales_endemicos_info_tablero()
        open_link(CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()], f'Canal Endémico para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()])

    elif virus_filter_can_end == 'Zika':
        
        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter_can_end}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter_can_end.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter_can_end}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter_can_end.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')
        
        st.markdown('-----')
        st.markdown('##### En el siguiente enlace puedes consultar los canales endémicos asociados y explorar las representaciones gráficas de la incidencia de diversas enfermedades.')
        st.markdown('''Esta herramienta te permitirá visualizar y analizar la incidencia actual en comparación con la incidencia histórica,
lo que facilitará la detección temprana de patrones anormales en los casos de enfermedad en estudio.''')
        open_link(CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()], f'Canal Endémico para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()])

    elif virus_filter_can_end == 'Chikungunya':
        
        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter_can_end}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter_can_end.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter_can_end}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter_can_end.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')

        st.markdown('-----')
        st.markdown('##### En el siguiente enlace puedes consultar los canales endémicos asociados y explorar las representaciones gráficas de la incidencia de diversas enfermedades.')
        st.markdown('''Esta herramienta te permitirá visualizar y analizar la incidencia actual en comparación con la incidencia histórica,
lo que facilitará la detección temprana de patrones anormales en los casos de enfermedad en estudio.''')
        open_link(CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()], f'Canal Endémico para {virus_filter_can_end}')
        show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter_can_end.upper()])

    else:
        canales_endemicos_info_general()
        st.markdown('-----')
        st.markdown('### :arrow_left: Por favor seleccione una de las enfermedades en el panel izquierdo para visualizar la información')
        st.markdown('##### Este portal posee información clasificada de la siguiente manera:')
        st.markdown('- Dengue')
        st.markdown('- Zika')
        st.markdown('- Chikungunya')
        st.markdown('-----')
        st.markdown('Al seleccionar uno de los virus específicos, tendrás acceso a información detallada sobre los canales endémicos asociados.')
