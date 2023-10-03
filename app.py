import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("india.csv")

st.sidebar.title("IndiaGraphiX")
option1 = st.sidebar.selectbox("Select",["Overall","State Wise"])

option2 = st.sidebar.selectbox("Select Parameter",["Basics","Workers","Religion","Household","Education","Age Wise","Power Parity"])

plot = st.sidebar.button("Show Results")
if plot:
    if option1 == "Overall":
        if option2 == "Basics":
            #POPULATION MAP
            st.title("Population")
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3, size="Population", size_max=9,
                                    mapbox_style="carto-positron")
            st.plotly_chart(fig)

            col1, col2 = st.columns(2)
            # MALE FEMALE PIECHART
            with col1:
                males = sum(df.Male)
                females = sum(df.Female)
                temp_df = pd.DataFrame({"Gender": ["male", "female"], "Population": [males, females]})
                fig = px.pie(temp_df, values='Population', names='Gender', title='Number of Males & Females ')
                fig.update_layout(width=350, height=350)
                st.plotly_chart(fig)
            with col2:
                males = sum(df.Male_Literate)
                females = sum(df.Female_Literate)
                temp_df = pd.DataFrame({"Gender": ["male", "female"], "Literates": [males, females]})
                fig = px.pie(temp_df, values='Literates', names='Gender', title='Literacy rate of Males & Females ')
                fig.update_layout(width=350, height=350)
                st.plotly_chart(fig)

            # SEX RATIO
            st.title("Sex Ratio of India")
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3, color="sex_ratio", size_max=9,color_continuous_scale = px.colors.cyclical.IceFire,
                                    mapbox_style="carto-positron")
            st.plotly_chart(fig)

            # LITERACY RATE
            st.title("Literacy Rate of  India")
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3, color="Litracy_rate", size_max=9,
                                    color_continuous_scale=px.colors.cyclical.IceFire,
                                    mapbox_style="carto-positron")
            st.plotly_chart(fig)





    else:
        pass