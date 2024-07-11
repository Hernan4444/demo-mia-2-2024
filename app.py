import altair as alt
import streamlit as st
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


def number_to_text(x):
    return "Si" if x == 1 else "No"


@st.cache_data
def load_data(data_path):
    print("Cargando datos")
    df = pd.read_csv(data_path)
    df.es_superhost = df.es_superhost.map(number_to_text)
    df.servicio_aire_acondicionado = df.servicio_aire_acondicionado.map(number_to_text)
    return df

@st.cache_data
def add_title_and_description():
    print("Cargando título")
    st.title("Demo - Airbnb (MIA 2024)")
    st.markdown("Realizada el 11 de Julio, vamos a explorar diferentes Airbnb de 10 ciudades")


def show_airbnb_dataframe(df):
    print("Dataset")
    camas = st.slider("Cantidad mínima de camas",
                      #min #max #value #step
                      1, 16, 16, 2)
    st.write("Camas: ", camas)
    st.write(df[df.capacidad >= camas])
    # st.dataframe(df)


def country_filter(df):
    pass


def show_airbnb_in_map(df, is_all_data):
    pass


def plot_days_of_week(df, column):
    pass


def plot_airbnb_by_superhost(df, column):
    pass


def interactive_view(df):
    pass


if __name__ == "__main__":
    df = load_data("Airbnb_Locations.csv")
    add_title_and_description()
    show_airbnb_dataframe(df)


    # Improvisar
    st.header("Improvisando en la marcha")
    pie = alt.Chart(df).mark_arc().encode(
        theta="count()", 
        color=alt.Color("es_superhost:N").scale(scheme="set2")
        )
    st.altair_chart(pie)

    # 1. Hacer un gráfico
    # 2. Subir a Github y publicar todo
    # 3. Esconder nustra página
    # 4. Hacer las demás cositas.
    
    # Descomentar a medida que avancemos

    # filtered_df = country_filter(df)
    # show_airbnb_in_map(filtered_df, filtered_df.shape == df.shape)
    # column_1, column_2 = st.columns(2)
    # plot_days_of_week(filtered_df, column_1)
    # plot_airbnb_by_superhost(filtered_df, column_2)
    # interactive_view(filtered_df)
