import streamlit as st

from typing import Callable, Dict


def principal():
    """
    Display the main title and classification of the collaborative dashboard.
    """
    st.title('Bienvenido al Tablero Colaborativo Integrador para Arbovirosis')
    st.markdown('### :arrow_left: Por favor seleccione uno de los portales en el panel izquierdo para visualizar la información')
    st.markdown('### Este tablero colaborativo posee información clasificada de la siguiente manera:')
    st.markdown('- Sivigila - INS')
    st.markdown('- Sivigila - Arbovirosis')
    st.markdown('- Entomologia')
    st.markdown('- Virologia')
    st.markdown('- Canales Endemicos')
    st.markdown('- Series de Tiempo')
    st.markdown('- Factores de Riesgo Ambiental')


def load_logos(ui_width: int, CONF: Dict, make_spaces: Callable):
    """
    Load and display logos in the user interface.

    Args:
        ui_width (int): Width of the user interface.
        CONF (Dict): Configuration data.
        make_spaces (Callable): Function to create empty spaces in the layout.
    """
    sivigila_logo, ins_logo, ops_logo, ministerio_logo, _temp_logo,_temp_logo_2 = st.columns([1, 1, 1, 1, 10, 5]
                                                                            if ui_width > 1400 else [1, 1, 2, 1, 2, 2])
    with sivigila_logo:
        st.image(CONF['LOGO_SIVIGILA'], width=70, caption="", use_column_width=False)
    with ins_logo:
        make_spaces(1)
        st.image(CONF['LOGO_INS'], width=120, caption="", use_column_width=False)
    with ops_logo:
        st.image(CONF['LOGO_OPS'], width=200, caption="", use_column_width=False)
    with ministerio_logo:
        make_spaces(1)
        st.image(CONF['LOGO_MINISTERIO'], width=200, caption="", use_column_width=False)
