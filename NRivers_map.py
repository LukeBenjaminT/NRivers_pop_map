import geopandas as gpd
import plotly.express as px
import streamlit as st

populated = gpd.read_file('populated.shp')

st.markdown('## Population Change in the Northern Rivers')
st.markdown("""
            The 2021 census shows the population of north-east NSW growing by more than 10% since the 2016 census.
However, parts of this diverse region have declined.
This map was created to show the biggest local changes between the two census.
It includes SA1 areas (the smallest available) with population greater than 200 and swing greater than 10%.

\nTotals for NE NSW:
- 355 707 people in the 2016 the census.
- 403 230 people in the 2021 the census.
- 13.36% population increase from 2016 to 2021.

Note: The 2021 census occured in unique circumstances which may impact data reliability.""")

fig = px.choropleth_mapbox(populated, 
                           geojson=populated.geometry, 
                           locations= populated.index, 
                           color=populated.pop_change,
                           color_continuous_scale="Picnic_r",
                           range_color=(-20, 20),
                           mapbox_style="stamen-toner",
                           zoom=6.8, 
                           center = {"lat": -29.3664, "lon": 153.0928},
                           opacity=0.5,
                           labels={'SA2_NAME21':'Location ',
                               'pop_change':'Population Change % ',
                                  'Tot_P_P_21':'2021 Population '},
                           custom_data = ['SA2_NAME21','Tot_P_P_21','pop_change']
                          )

fig.update_traces(hovertemplate =
                            '<b>%{customdata[0]}</b>'+
                            '<br><b>2021 Population</b>: %{customdata[1]}<br>'+
                            '<b>Change since 2016</b>: %{customdata[2]:.2f}%',
                  marker_line_width=0)


fig.update_geos(fitbounds="locations", visible=False).update_layout(
    margin={"l": 0, "r": 0, "t": 0, "b": 0}
)

st.plotly_chart(fig, use_container_width=False, sharing="streamlit", theme="streamlit")
