import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.set_page_config(layout="wide")
st.title("Análisis de Terremotos (2023–2024) 🌍")

# Carregar dados
@st.cache_data
def carregar_dados():
    df = pd.read_parquet("terremotos.parquet")
    return df

df = carregar_dados()

# Filtros na lateral
st.sidebar.title("Filtros 🔍")

anos_disponiveis = sorted(df['ano'].unique())
ano_selecionado = st.sidebar.radio("Seleccione el año", anos_disponiveis)

mag_min, mag_max = float(df['magnitude'].min()), float(df['magnitude'].max())
magnitude = st.sidebar.slider("Magnitud mínima", mag_min, mag_max, 6.0)

# Filtragem dos dados
df_filtrado = df[(df['ano'] == ano_selecionado) & (df['magnitude'] >= magnitude)]

# Criação de mapa
st.subheader(" Mapa de los terremotos")

fig_mapa = px.scatter_geo(
    df_filtrado,
    lat='latitude',
    lon='longitude',
    color='magnitude',
    hover_name='pais',
    size='magnitude',
    size_max=14,
    projection='natural earth',
    color_continuous_scale='YlOrRd',
    template='plotly_dark'  # Estilo escuro para combinar com o Streamlit dark
)

fig_mapa.update_layout(
    geo=dict(
        showland=True,
        landcolor='rgb(30,30,30)',   # Terreno escuro
        showocean=True,
        oceancolor='rgb(15, 30, 80)',  # Oceano escuro
        showcountries=True,
        countrycolor='gray'
    ),
    margin=dict(l=0, r=0, t=30, b=0),
    height=650,
    coloraxis_colorbar=dict(
    title=dict(text='Magnitud', font=dict(color='white')),
    tickvals=[6.5, 7, 7.5, 8],
    tickfont=dict(color='white')
)
    )

fig_mapa.update_traces(
    marker=dict(
        line=dict(width=0.5, color='black'),
        opacity=0.85
    )
)

st.plotly_chart(fig_mapa, use_container_width=True)

# Tabela top 10
st.subheader("Top 10 regiones con más terremotos")
top_locais = df_filtrado['local'].value_counts().reset_index()
top_locais.columns = ['Local', 'Cantidad']  # em espanhol, se preferir
st.dataframe(top_locais.head(10))

# Gráfico
st.markdown("---")
st.subheader("📊 Distribución de magnitud y profundidad")

col1, col2 = st.columns(2)

# Histograma da magnitude
with col1:
    st.markdown("**Distribución de magnitud**")
    fig_mag = px.histogram(df_filtrado, x="magnitude", nbins=30, color_discrete_sequence=["#F4A460"])
    fig_mag.update_layout(xaxis_title="Magnitude", yaxis_title="Contagem")
    st.plotly_chart(fig_mag, use_container_width=True)

# Histograma da profundidade
with col2:
    st.markdown("**Distribución de profundidad**")
    fig_dep = px.histogram(df_filtrado, x="profundidade_km", nbins=30, color_discrete_sequence=["skyblue"])
    fig_dep.update_layout(xaxis_title="Profundidade (km)", yaxis_title="Contagem")
    st.plotly_chart(fig_dep, use_container_width=True)

# Correlação
st.subheader("Correlación entre profundidad y magnitud")
fig_corr = px.scatter(df_filtrado, x="profundidade_km", y="magnitude",
                      color="magnitude",
                      opacity=0.6,
                      color_continuous_scale="OrRd")
fig_corr.update_layout(xaxis_title="Profundidade (km)", yaxis_title="Magnitude")
st.plotly_chart(fig_corr, use_container_width=True)

# Información
st.markdown("---")
st.subheader("🔎 Información general")

total_eventos = len(df_filtrado)
media_magnitude = df_filtrado['magnitude'].mean()
local_mais_afetado = df_filtrado['local'].value_counts().idxmax() if total_eventos > 0 else "N/A"
qtd_local_mais_afetado = df_filtrado['local'].value_counts().max() if total_eventos > 0 else 0

st.markdown(f"""
- **Total de terremotos** registrados en {ano_selecionado} con magnitud superior a {magnitude}: **{total_eventos}**
- **Magnitud media** de los terremotos filtrados: **{media_magnitude:.2f}**
- **Región más afectada**: **{local_mais_afetado}** con **{qtd_local_mais_afetado}** ocurrencias
""")

# Mensagem adicional
if total_eventos == 0:
    st.warning("⚠️ No se encontraron terremotos con estos criterios. Intente ajustar los filtros.")
elif media_magnitude > 6.5:
    st.success("✅ Predominan magnitudes elevadas, lo que indica eventos de mayor severidad.")
else:
    st.info("ℹ️ La mayoría de los eventos presentan una magnitud moderada.")

# Rodapé
st.markdown("---")
st.markdown("Desarrollado con datos de la [USGS API](https://earthquake.usgs.gov/fdsnws/event/1/)")
st.markdown("Enlace para ver terremotos en vivo(https://earthquake.usgs.gov/earthquakes/map/)")