# Importamos librerias necesarias
import requests
import plotly.express as px
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# GUardamos la consulta en un variable
url = "https://earthquake.usgs.gov/earthquakes"
url += "/feed/v1.0/summary/all_hour.geojson"

# Indicamos la version
headers = {"Acept": "https://earthquake.usgs.gov/earthquakes/feed/v1.0"}

# Le pasamos la url de la consulta de la API y la version de la misma
r = requests.get(url, headers=headers)

# Imprimimos status code esperando 200 para saber
# si la solicitud se realizo correctamente
print(f"Status Code: {r.status_code}")

# Transformamos la informacion de objetos a diccionarios
data = r.json()

# Sacamos cada uno de los terremostos que estan en el diccionario para
# trabajar con la informacion
features = data['features']

# Creamos listas de los datos que queremos graficar
mags, lats, lons, titles = [], [], [], []

# Recoremos los datos y los guardamos en listas
for i in features:
    mag = i['properties']['mag']

    if mag is None or mag < 0:
        continue
    else:
        mags.append(float(i['properties']['mag']))
        lons.append(float(i['geometry']['coordinates'][0]))
        lats.append(float(i['geometry']['coordinates'][1]))
        titles.append(i['properties']['title'])

# Creamos el titulo del projecto o sea de la grafica Titulo principal
project_title = "Real Time Earthquake Monitor - Earthquakes in the last hour"

# Creamos el gráfico
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=project_title,
    color=mags,
    projection='natural earth',
    color_continuous_scale='viridis',
    )

# Perzonalizacion
fig.update_layout(title_font_size=28)

st.set_page_config(layout="wide")

st_autorefresh(interval=60000, key="earthquake_refresh")

# Mostrar gráfico
st.plotly_chart(fig, use_container_width=True)
