import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import time

st.set_page_config(page_title='India Census 2011 Info', page_icon='logo-g050300332_640.png', layout='wide')
df = pd.read_csv('india.csv')
list_of_state = df['State'].unique().tolist()
list_of_state.insert(0, 'Overall India')

st.title('India Census 2011 Visualization')

st.subheader('*Note!* :sunglasses:')
st.write('**Size show first parameter** ')
st.write('**Color show Second parameter** ')


st.sidebar.title('Options')
selected_state = st.sidebar.selectbox('Select a Options', list_of_state)
primary = st.sidebar.selectbox('Select First Parameter', sorted(df.columns[2:]))
secondary = st.sidebar.selectbox('Select Second Parameter', sorted(df.columns[2:]))

state = st.sidebar.button("Plot Graph")

if state:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=2.9, mapbox_style="carto-positron", width=500,
                                height=600, size_max=26, size=primary, color=secondary, hover_name='District',
                                color_continuous_scale='plasma')
        fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=2.9, mapbox_style="carto-positron", width=500,
                                height=600, size_max=26, size=primary, color=secondary, hover_name='District',
                                color_continuous_scale='plasma')
        fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})

        st.plotly_chart(fig, use_container_width=True)


