#  Temblores del planeta: Explorando datos sísmicos 🌎
### Análisis Exploratorio de Terremotos (2023-2024) - API USGS 

#### 📈 Descripción del Proyecto

Los terremotos ocurren cuando hay una liberación repentina de energía en el interior de la Tierra.
Según el Centro Nacional de Información sobre Terremotos (NEIC), se registran alrededor de 20.000 terremotos al año en todo el mundo —un promedio de 55 por día.
Hasta hoy, ningún gran terremoto ha sido predicho con antelación por la ciencia.

Este proyecto consiste en la recolección y análisis exploratorio de datos de terremotos ocurridos entre 2023 y 2024 a nivel mundial, utilizando datos públicos de la API del USGS (Servicio Geológico de los Estados Unidos).
El objetivo es identificar patrones en la frecuencia, ubicación, magnitud y profundidad de los sismos.

Además, se desarrolló un dashboard interactivo con Streamlit para facilitar la visualización e interpretación de los resultados:

![mapa-streamlit](https://github.com/user-attachments/assets/a16cf6a8-ef13-4c7a-97f5-d3bc80e29ba8)

Figura 1. Mapa interactivo de los terremotos en Streamlit.



#### 🧱Estructura del proyecto

* Obtención automática de datos desde la API pública del USGS

* Limpieza y preprocesamiento de datos para análisis

* Análisis descriptivo de magnitud, profundidad y frecuencia de los terremotos

* Visualizaciones gráficas (distribución de magnitudes, profundidades, mapa)

* Dashboard interactivo para exploración



#### ⚠️ Resultados principales

* El año 2023 hubo más terremotos que el año 2024.

* La mayoría de los terremotos registrados tienen magnitud entre 4,5 y 5,0 (ligeros a moderados).

* No se registraron terremotos devastadores en el período analizado.

* El terremoto con mayor magnitud ocurrió en 2023 en la región de Turquía con una magnitud de 7,8 y su profundidad fue de apenas 10 km.

* El terremoto más profundo presentó una profundidad de 653,8 km y su magnitud fue de 4,5, considerado ligero según la escala Richter.

* No existe correlación significativa entre profundidad y magnitud.

* Las regiones insulares en los bordes de las placas tectónicas concentran la mayor actividad sísmica.

* Se observan picos de actividad en ciertos meses y horas, posiblemente asociados a zonas tectónicas activas. Aunque no siguen un patrón fijo, es interesante notar concentraciones de eventos en determinados momentos —posiblemente vinculados a zonas tectónicas activas.

#### 📁 Estructura del Repositorio
earthquake-project.ipynb/ : notebook de Jupyter con análisis exploratorio

app.py : código del dashboard Streamlit

requirements.txt : dependencias del proyecto

README.md : documentación del proyecto


#### 🛠️ Tecnologías Utilizadas

Python: Utilizando las siguientes librerías - requests, pandas,cartopy, matplotlib, seaborn, plotly, streamlit

API USGS Earthquake Catalog: 

https://earthquake.usgs.gov/fdsnws/event/1/


#### 📎Seguimiento de terremotos en tiempo real:

https://earthquake.usgs.gov/earthquakes/map/


#### 📬Contacto

Para dudas o sugerencias, contáctame en:

LinkedIn: www.linkedin.com/in/ariel-felix

