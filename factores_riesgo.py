import streamlit as st

from streamlit_option_menu import option_menu
from typing import Callable


def factores_riesgo(ui_width: int, CONF: dict, open_link: Callable):
    """
    Display the Factores de Riesgo Ambiental section.

    Args:
        ui_width (int): Width of the UI.
        CONF (dict): Configuration dictionary.
        open_link (callable): Function to open a link.
    """
    st.markdown(f'# Factores de Riesgo Ambiental')

    riesgo_specific = option_menu(
        menu_title=None,
        options=['Portal Dengue', 'Boletín Clima y Salud', 'GeoVisor Sivigila'],
        orientation='horizontal',
        default_index=0,
        styles={'container': {'background-color': 'transparent'}})

    _temp_logo, riesgo_banner, _temp_logo_2 = st.columns([2, 8, 1] if ui_width > 1400 else [2, 8, 1])
    with riesgo_banner:
        st.image(CONF['RIESGO_AMB_BANNER'], caption="", width=900 if ui_width > 1400 else 600) 

    if riesgo_specific == 'Portal Dengue':
        st.markdown('##### Información relevante del portal Dengue:')
        open_link(CONF['RIESGO_AMBIENTAL']['DENGUE'], 'Portal Dengue')
        st.markdown('''
                    Tablero que tiene en cuenta las alertas históricas ambientales para lluvias y aumento de temperaturas reportadas por IDEAM a escala municipal;
                    comparando y analizando su intensidad, cantidad y cronología, el comportamiento nacional, departamental y municipal del evento, el canal endémico, la tendencia de las últimas 4 semanas epidemiológicas, la presencia del vector y transmisibilidad de la enfermedad a escala municipal, generando un indicador de riesgo para los próximos 15 días, el cual se actualiza diariamente.
                    ''')

    if riesgo_specific == 'Boletín Clima y Salud':
        st.markdown('##### Información relevante del portal Boletín de Clima y Salud:')
        open_link(CONF['RIESGO_AMBIENTAL']['CLIMA_SALUD'], 'Boletín Clima y Salud')

    if riesgo_specific == 'GeoVisor Sivigila':
        st.markdown('### GeoVisor Sivigila')
        open_link(CONF['RIESGO_AMBIENTAL']['GEOVISOR'], 'Geovisor')
        st.markdown('Su objetivo es facilitar los análisis geográficos o espaciales de los eventos de interés en salud publica dentro del territorio nacional, visualizando la distribución y comportamiento de los casos georreferenciados y otras variables; con el fin de que las Entidades Territoriales implementen acciones de vigilancia, control, mitigación y aporte información para la toma de decisiones.')
