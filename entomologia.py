import os
import streamlit as st

from typing import Optional, Callable


def entomologia_sidebar(CONF: dict, open_link: Callable) -> Optional[bool]:
    """
    Display the sidebar for the entomology section.

    Args:
        CONF (dict): Configuration data.
        open_link (Callable): Function to open a link.

    Returns:
        Optional[bool]: True if the "Cargar Tablero Aqui" button is clicked, otherwise None.
    """
    cargar_tablero = None
    entomologia_tableros = st.selectbox('Tableros Power BI:', options=['', "Levantamientos entomologicos", 'Resistencia a Insecticidas', 'Muestras'])
    if entomologia_tableros != '':
        open_link(CONF['ENTOMOLOGIA']['TABLERO_' + entomologia_tableros.upper().replace(' ', '_')], 'Tablero de ' + entomologia_tableros)
        cargar_tablero = st.button('Cargar Tablero Aqui')        

    entomologia_circulares = st.selectbox('Circulares:', options=CONF['ENTOMOLOGIA']['CIRCULARES'])
    if entomologia_circulares != '':
        split_ = entomologia_circulares.split()

        with open(os.path.join(CONF['ENTOMOLOGIA']['CARPETA_ENTOMOLOGIA'], f'CIRCULAR CONJUNTA EXTERNA {split_[1]} {split_[-1]}.pdf'), 'rb') as f:
            st.download_button(f'Circulares {entomologia_circulares}', f, file_name=f'Circulares {entomologia_circulares}.pdf')

    entomologia_rep_anuales = st.selectbox('Reportes Anuales Arbovirosis:', options=CONF['ENTOMOLOGIA']['REP_ANUALES'])
    if entomologia_rep_anuales != '':

        with open(os.path.join(CONF['ENTOMOLOGIA']['CARPETA_ENTOMOLOGIA'], f'REPORTE ARBOVIROSIS {entomologia_rep_anuales}.pdf'), 'rb') as f:
            st.download_button(f'Reporte Anual Arbovirosis {entomologia_rep_anuales}', f, file_name=f'Reporte Anual Arbovirosis {entomologia_rep_anuales}.pdf')

    entomologia_res_insecticidas = st.selectbox('Reportes Anuales Resistencia a Insecticidas:', options=CONF['ENTOMOLOGIA']['INSECTICIDAS'])
    if entomologia_res_insecticidas != '':

        with open(os.path.join(CONF['ENTOMOLOGIA']['CARPETA_ENTOMOLOGIA'], f'REPORTE INSECTICIDAS {entomologia_res_insecticidas}.pdf'), 'rb') as f:
            st.download_button(f'Reporte Anual Insecticidas {entomologia_res_insecticidas}', f, file_name=f'Reporte Anual Insecticidas {entomologia_res_insecticidas}.pdf')

    entomologia_protocolos = st.selectbox('Protocolos:', options=CONF['ENTOMOLOGIA']['PROTOCOLOS'])
    if entomologia_protocolos != '':

        with open(os.path.join(CONF['ENTOMOLOGIA']['CARPETA_ENTOMOLOGIA'], f'PROTOCOLO {entomologia_protocolos}.pdf'), 'rb') as f:
            st.download_button(f'Protocolo {entomologia_protocolos}', f, file_name=f'Protocolo {entomologia_protocolos}.pdf')

    st.markdown('-----')
    open_link(CONF['ENTOMOLOGIA']['BIBLIOGRAFIA'], 'Bibliografia')
    return cargar_tablero, entomologia_tableros


def entomologia(ui_width: int, CONF: dict, show_link: Callable, cargar_tablero: Optional[bool] = None, entomologia_tablero: Optional[str] = None):
    """
    Display the entomology section.

    Args:
        ui_width (int): Width of the user interface.
        CONF (dict): Configuration data.
        show_link (Callable): Function to show a link.
        cargar_tablero (bool, optional): Whether the "Cargar Tablero Aqui" button was clicked. Defaults to None.
        entomologia_tablero (str, optional): Type of entomology dashboard selected. Defaults to None.
    """
    st.markdown('# Bienvenido al Tablero Colaborativo Integrador para Entomología')
    st.markdown('''***Aedes aegypti*** (Linnaeus, 1762) es una especie de zancudo originaria de África, la cual se desplazó hasta el Nuevo Mundo en los barcos
de comercio de esclavos entre los siglos XV y XVIII. Una vez se estableció poblacionalmente en las zonas costeras de las Américas, se
dispersó rápidamente hacia el interior del continente (Bruzzone & Utgés, 2022; Ruiz-López et al., 2016). Debido a que presenta hábitos
urbanos y antropofílicos, esta especie se ha establecido como el principal vector de los arbovirus del dengue (DENV 1-4) (Bhatt et al.,
2013; Bruzzone & Utgés, 2022; Castrillón et al., 2014; Rodríguez Cruz, 2002) y de los alfavirus del chikungunya (CHIKV) y Zika (ZIKV). La
transmisión de estas enfermedades representa un tema de importancia en salud pública internacional debido al número de casos
reportados anualmente y a que no existe vacuna para estas patologías (Bruzzone & Utgés, 2022; Rodriguez-Morales, 2015ª, 2015b;
Weaver & Lecuit, 2015).''')

    _temp_logo, entomologia_image, _temp_logo2 = st.columns([2, 8, 1] if ui_width > 1400 else [2, 8, 1])
    with entomologia_image:
        st.image(CONF['ENTOMOLOGIA']['IMAGEN'], caption="", width=700 if ui_width > 1400 else 500) 
    if cargar_tablero:
        show_link('Tablero de ' + entomologia_tablero, CONF['ENTOMOLOGIA']['TABLERO_' + entomologia_tablero.upper().replace(' ', '_')], True)
