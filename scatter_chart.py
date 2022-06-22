# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:07:42 2022

@author: Abhinav Bhamidipati
"""

import plotly.graph_objects as go #create figure
import plotly.express as px #create gapminded dataset

from plotly.offline import init_notebook_mode, plot
init_notebook_mode()


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")

fig = go.Figure()

fig.add_trace(go.Scatter(x = df['year'], y = df['lifeExp'], mode = 'markers'))
fig.add_trace(go.Scatter(x = df2['year'], y = df2['lifeExp'], mode = 'lines'))

fig.update_layout(title='Life Expectancy over the years',
                  xaxis_title = 'Years',
                  yaxis_title = 'Life Expectancy')



plot(fig)