# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:06:35 2022

@author: Abhinav Bhamidipati
"""

import plotly.express as px #create gapminded dataset
from plotly.offline import init_notebook_mode, plot
init_notebook_mode()

# df = px.data.election()
# geojson = px.data.election_geojson()


# fig = px.choropleth(df, geojson = geojson, locations = 'district', featureidkey= 'properties.district',
#                     projection = 'mercator', color = 'Bergeron')

# fig.update_geos(fitbounds = 'locations', visible = False)

df = px.data.gapminder().query('year == 2007')

fig = px.choropleth(df, locations='iso_alpha', color = 'lifeExp', 
                    hover_name = 'country',
                    projection = 'orthographic', #change map to globe
                    color_continuous_scale=px.colors.sequential.Plasma)

plot(fig)
