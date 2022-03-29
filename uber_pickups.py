import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
st.title('Uber pickups in Coimbatore')
DATE_COLUMN = 'date/time'
def load_data(nrows):
    data = pd.read_csv('uberdata.csv', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Create a text element and let the reader know that the data is loading
data_load_state=st.text('Loading Data..')

#Load 10,000 rows of data into the dataframe
data=load_data(10000)

#Notify the reader that the data was successfully loaded
data_load_state.text('Loading Data..Done')

#Print the raw data
st.subheader('Raw Data')
st.write(data)

#Print a Histogram
st.subheader('Number of Pickups by hour')

hist_values =np.histogram(data[DATE_COLUMN].dt.hour,bins=24)[0]

st.bar_chart(hist_values)

st.subheader('Map of all Pickups')

st.map(data, zoom=14)