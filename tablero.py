import streamlit as st
import streamlit_javascript as st_js

from envyaml import EnvYAML

from canales_endemicos import (canales_endemicos_info_general, canales_endemicos_info_tablero,
                            #    load_image,
                               canales_endemicos_sidebar, canales_endemicos)
from sivigila_arbovirosis import titulo, sivigila_arbovirosis_sidebar, sivigila_arbovirosis
from series_tiempo import series_tiempo, series_tiempo_sidebar

from factores_riesgo import factores_riesgo
from entomologia import entomologia, entomologia_sidebar
from sivigila import sivigila, sivigila_sidebar
from principal import principal, load_logos

st.set_page_config(layout="wide", page_title="Tablero Colaborativo INS",
                   page_icon=":information_source:")

CONF = EnvYAML('tablero.yaml')
main_filter, virus_filter = None, None

# LOGOS
ui_width = st_js.st_javascript("window.innerWidth")


def render_background() -> str:
    """
    Render the background style.

    Returns:
        str: Background style HTML.
    """
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({CONF['BACKGROUND']});
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """, unsafe_allow_html=True)
    return ''


def make_spaces(lines: int):
    """
    Add line breaks.

    Args:
        lines (int): Number of line breaks.
    """
    for i in range(lines):
        st.markdown('\n')


def open_link(url: str, text: str):
    """
    Display an open link button.

    Args:
        url (str): The URL to open.
        text (str): The button text.
    """
    button_html = f'<a href="{url}" style="background-color: #66b0ff; color: white; padding: 8px 16px; border-radius: 4px; text-decoration: none;">{text}</a>'
    st.markdown(button_html, unsafe_allow_html=True)
   
    
def show_link(title: str, url: str, bypass: bool = False):
    """
    Display a link.

    Args:
        title (str): The link title.
        url (str): The URL to display.
        bypass (bool, optional): Bypass link. Defaults to False.
    """
    if bypass:
        iframe_code = f'''
            <iframe title="{title}" width="{ui_width}" height="{ui_width/2}" src="{url}" frameborder="0" allowFullScreen="true"></iframe>
            '''
        st.markdown(iframe_code, unsafe_allow_html=True)
    else:
        if st.button(title):
            iframe_code = f'''
            <iframe title="{title}" width="{ui_width}" height="{ui_width/2}" src="{url}" frameborder="0" allowFullScreen="true"></iframe>
            '''
            st.markdown(iframe_code, unsafe_allow_html=True)

load_logos(ui_width, CONF, make_spaces)

# SIDEBAR
with st.sidebar:

    st.markdown('### Opciones del Tablero Colaborativo')
    main_filter = st.selectbox('Seleccione el portal para explorar la información:', options=[
        "", 'Sivigila - INS', 'Sivigila - Arbovirosis', 'Entomología', 'Virología', 'Canales Endémicos', 'Series de Tiempo', 'Factores de Riesgo Ambiental'])
    
    if main_filter == 'Sivigila - Arbovirosis':

        virus_filter = sivigila_arbovirosis_sidebar(open_link, CONF)
    
    elif main_filter == 'Sivigila - INS':

        sivigila_sidebar(CONF, open_link)
    
    elif main_filter == 'Entomología':

        cargar_tablero_entomologia, entomologia_tablero = entomologia_sidebar(CONF, open_link)

    elif main_filter == 'Canales Endémicos':
        
        virus_filter_can_end = canales_endemicos_sidebar()
    
    elif main_filter == 'Series de Tiempo':
        
        virus_filter_can_end = series_tiempo_sidebar()

# DASHBOARD
if main_filter == 'Sivigila - INS':

    render_background() if ui_width > 350 else None
    sivigila(CONF, open_link)

elif main_filter == 'Sivigila - Arbovirosis':

    titulo(virus_filter)
    make_spaces(3)
    sivigila_arbovirosis(virus_filter, CONF, open_link, show_link, render_background if ui_width > 350 else None,
                         canales_endemicos_info_general, canales_endemicos_info_tablero)

elif main_filter == 'Entomología':

    render_background() if ui_width > 350 else None
    entomologia(ui_width, CONF, show_link,
                cargar_tablero_entomologia if cargar_tablero_entomologia else None,
                entomologia_tablero if entomologia_tablero else None)

elif main_filter == 'Virología':

    render_background() if ui_width > 350 else None
    st.markdown('# Virología')
    st.markdown('### :arrow_left: Por favor seleccione una de las enfermedades en el panel izquierdo para visualizar la información')

elif main_filter == 'Canales Endémicos':

    render_background() if ui_width > 350 else None
    # load_image(virus_filter_can_end)
    make_spaces(3)
    canales_endemicos(virus_filter_can_end, CONF, open_link, show_link)
    
elif main_filter == 'Series de Tiempo':

    render_background() if ui_width > 350 else None
    # load_image(virus_filter_can_end)
    make_spaces(3)
    series_tiempo(virus_filter_can_end, CONF, open_link, show_link)

elif main_filter == 'Factores de Riesgo Ambiental':

    render_background() if ui_width > 350 else None
    factores_riesgo(ui_width, CONF, open_link)

else:

    render_background() if ui_width > 350 else None
    principal()
