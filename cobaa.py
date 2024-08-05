import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

st.write("This the map")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# df = pd.DataFrame({
#     "lat": [110.3864],
#     "lon": [-7.7733],
#     "city": ["UNY"]
# })

# st.map(df)

# Data koordinat kota besar
data = {
    'lat': [-74.0060, -118.2437, -0.1278, 139.6917, 151.2093, 110.3864],  # Longitude
    'lon': [40.7128, 34.0522, 51.5074, 35.6895, -33.8688, -7.7733],  # Latitude
    'city': ['New York', 'Los Angeles', 'London', 'Tokyo', 'Sydney', 'UNY']
}


df = pd.DataFrame(data)

# Membuat peta folium
m = folium.Map(location=[df['lon'].mean(), df['lat'].mean()], zoom_start=15)

# Menambahkan titik dan jalur
folium.PolyLine(locations=df[['lon', 'lat']].values, color='blue').add_to(m)
for i, row in df.iterrows():
    folium.Marker(location=[row['lon'], row['lat']], popup=row['city']).add_to(m)

# Menampilkan peta di Streamlit
st_folium(m, width=700, height=500)

# # Membuat DataFrame
# df = pd.DataFrame(data)

# # Menampilkan peta dengan koordinat tertentu
# st.map(df)

# # Menampilkan DataFrame di aplikasi Streamlit (opsional)
# st.write(df)