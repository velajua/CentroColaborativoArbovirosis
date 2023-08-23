import streamlit as st

from streamlit_option_menu import option_menu
from typing import Callable, Dict, Optional


def titulo(virus_filter: str):
    """
    Display the title based on the selected virus filter.

    Args:
        virus_filter (str): The selected virus filter.
    """
    st.markdown(f'# Sivigila - Arbovirosis{" - " if virus_filter else ""}{virus_filter}')


def sivigila_arbovirosis_sidebar(open_link: Callable, CONF: Dict) -> Optional[str]:
    """
    Display the sidebar for Sivigila - Arbovirosis and handle user selection.

    Args:
        open_link (Callable): Function to open a link.
        CONF (Dict): Configuration data.

    Returns:
        Optional[str]: The selected virus filter.
    """
    virus_filter = st.selectbox('Seleccione el virus:', options=["", 'Dengue', 'Zika', 'Chikungunya'])
    
    if virus_filter:
        st.markdown('-----')
        open_link(CONF['PROTOCOLOS'][virus_filter.upper()], f'Protocolo para {virus_filter}')
        open_link(CONF['INFORME_EVENTO'][virus_filter.upper()], f'Informe Evento {virus_filter}')
        open_link(CONF['FICHA_NOTIFICACION'][virus_filter.upper()], f'Ficha de Notificación para {virus_filter}')

    else:
        st.markdown('-----')
        open_link(CONF['LINIAMIENTOS'], f'Liniamientos')

    return virus_filter


def sivigila_dengue():
    """
    Display information about Dengue.
    """
    st.markdown('''
        Dengue es una enfermedad viral aguda que puede afectar a personas de cualquier edad, especialmente niños y adultos mayores, causada por un virus transmitido a través de la picadura de mosquitos infectados (Aedes aegypti).
        ''')
    st.markdown('''
        Los mosquitos del dengue se presentan en zonas urbanas con altitudes inferiores a altura 2314 sobre el nivel del mar y una temperatura media entre 20°C y 25°C, ponen sus huevos en depósitos de agua limpia como albercas, floreros de plantas acuáticas, llantas, baldes de agua y cualquier recipiente que está a la intemperie y que puede almacenar agua.
        ''')


def sivigila_indicadores_dengue():
    """
    Display information about Dengue Indicators.
    """
    st.markdown('''
        El tablero informativo constituye una herramienta fundamental para el análisis y seguimiento de los indicadores de Dengue. Con un enfoque claro en la utilidad y accesibilidad de los datos, este sistema permite a los usuarios separar y filtrar la información por departamento, brindando una visión más precisa de la incidencia del Dengue, Dengue grave y las mortalidades asociadas en cada región. Además, resulta especialmente valioso para observar y comparar el comportamiento de dichos indicadores a lo largo de los años, facilitando así la detección de patrones y tendencias epidemiológicas. Gracias a esta funcionalidad, los profesionales de la salud, autoridades y demás actores interesados pueden tomar decisiones informadas y diseñar estrategias efectivas para la prevención y control de esta enfermedad transmitida por vectores.
        ''')


def sivigila_arbovirosis(virus_filter: str, CONF: Dict, open_link: Callable, show_link: Callable,
                         render_background: Optional[Callable], canales_endemicos_info_general: Callable,
                         canales_endemicos_info_tablero: Callable):
    """
    Display information and content for Sivigila - Arbovirosis.

    Args:
        virus_filter (str): The selected virus filter.
        CONF (Dict): Configuration data.
        open_link (Callable): Function to open a link.
        show_link (Callable): Function to show a link.
        render_background (Optional[Callable]): Function to render background content.
        canales_endemicos_info_general (Callable): Function to show general information about canales endémicos.
        canales_endemicos_info_tablero (Callable): Function to show information about the canales endémicos tablero.
    """
    if virus_filter == 'Dengue':
        
        sivigila_dengue()

        info_specific = option_menu(
            menu_title=None,
            options=['Tabla Indicadores', 'Canales Endémicos'],
            orientation='horizontal',
            default_index=0)
        
        st.markdown(f'##### El tablero de información del INS sobre {virus_filter} puede ser encontrado en el siguiente enlace:')
        open_link(CONF['TABLERO_POWER_BI_INS'][virus_filter.upper()], f'Tablero de {virus_filter} - INS')
        
        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')

        if info_specific == 'Tabla Indicadores':
            st.markdown('-----')
            st.markdown(f'##### El tablero de indicadores para {virus_filter} puede ser encontrado en el siguiente enlace:')
            open_link(CONF['TABLERO_INDICADORES'][virus_filter.upper()], 'Tablero de Indicadores')
            sivigila_indicadores_dengue()
            show_link('Cargar Tablero Aqui', CONF['TABLERO_INDICADORES'][virus_filter.upper()])
        elif info_specific == 'Canales Endémicos':
            st.markdown('-----')
            st.markdown(f'##### Los canales endemicos para {virus_filter} pueden ser encontrado en el siguiente enlace:')
            open_link(CONF['CANALES_ENDEMICOS'][virus_filter.upper()], 'Canales Endémicos')
            canales_endemicos_info_tablero()
            show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter.upper()])
        
    elif virus_filter == 'Zika':
        
        info_specific = option_menu(
            menu_title=None,
            options=['Tabla Indicadores', 'Canales Endémicos'],
            orientation='horizontal',
            default_index=0)

        st.markdown(f'##### El tablero de información del INS sobre {virus_filter} puede ser encontrado en el siguiente enlace:')
        open_link(CONF['TABLERO_POWER_BI_INS'][virus_filter.upper()], f'Tablero de {virus_filter} - INS')
            
        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')

        if info_specific == 'Tabla Indicadores':
            st.markdown('-----')
            st.markdown(f'##### El tablero de indicadores para {virus_filter} puede ser encontrado en el siguiente enlace:')
            open_link(CONF['TABLERO_INDICADORES'][virus_filter.upper()], 'Tablero de Indicadores')
            st.markdown(f'El tablero posee información relevante de los indicadores de {virus_filter}')
            show_link('Cargar Tablero Aqui', CONF['TABLERO_INDICADORES'][virus_filter.upper()])

        elif info_specific == 'Canales Endémicos':
            st.markdown('-----')
            st.markdown(f'##### Los canales endemicos para {virus_filter} pueden ser encontrado en el siguiente enlace:')
            open_link(CONF['CANALES_ENDEMICOS'][virus_filter.upper()], 'Canales Endémicos')
            show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter.upper()])

    elif virus_filter == 'Chikungunya':
        
        info_specific = option_menu(
            menu_title=None,
            options=['Tabla Indicadores', 'Canales Endémicos'],
            orientation='horizontal',
            default_index=0)

        st.markdown(f'##### El tablero de información del INS sobre {virus_filter} puede ser encontrado en el siguiente enlace:')
        open_link(CONF['TABLERO_POWER_BI_INS'][virus_filter.upper()], f'Tablero de {virus_filter} - INS')

        periodo__ = st.selectbox(f'Seleccione el periodo de visualización del informe para {virus_filter}', options=CONF['SIVIGILA_VISUALIZACION_INFORMES_PERIODO'][virus_filter.upper()])
        ano__ = st.selectbox(f'Seleccione el año de visualización del informe para {virus_filter}', options=CONF['ANOS_INFORME'])
        if periodo__:
            open_link(CONF['ENLACE_INFORMES'].replace('-VECTOR-', virus_filter.upper()).replace('-PERIODO-', periodo__).replace('-ANO-', ano__), 'Ver Informe')

        if info_specific == 'Tabla Indicadores':
            st.markdown('-----')
            st.markdown(f'##### El tablero de indicadores para {virus_filter} puede ser encontrado en el siguiente enlace:')
            open_link(CONF['TABLERO_INDICADORES'][virus_filter.upper()], 'Tablero de Indicadores')
            st.markdown(f'El tablero posee información relevante de los indicadores de {virus_filter}')
            show_link('Cargar Tablero Aqui', CONF['TABLERO_INDICADORES'][virus_filter.upper()])

        elif info_specific == 'Canales Endémicos':
            st.markdown('-----')
            st.markdown(f'##### Los canales endemicos para {virus_filter} pueden ser encontrado en el siguiente enlace:')
            open_link(CONF['CANALES_ENDEMICOS'][virus_filter.upper()], 'Canales Endémicos')
            show_link('Cargar Tablero Aqui', CONF['CANALES_ENDEMICOS'][virus_filter.upper()])

    else:

        render_background() if render_background else None
        st.markdown('##### :arrow_left: Por favor seleccione una de las enfermedades en el panel izquierdo para visualizar la información')
        st.markdown('##### Este portal posee información clasificada de la siguiente manera:')
        st.markdown('- Dengue')
        st.markdown('- Zika')
        st.markdown('- Chikungunya')
        st.markdown('-----')
        st.markdown('Al seleccionar uno de los virus específicos, tendrás acceso a una tabla completa de indicadores e información detallada sobre los canales endémicos asociados.')
        canales_endemicos_info_general()
