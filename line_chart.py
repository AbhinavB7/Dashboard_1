# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:56:42 2022

@author: 91704
"""

import plotly.graph_objects as go #create figure
import plotly.express as px #create gapminded dataset

from plotly.offline import init_notebook_mode, plot
init_notebook_mode()


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")

fig = go.Figure(data = [go.Scatter(x = df['year'], y = df['lifeExp'],\
                                   line = dict(color = 'blue', width= 4), text = df['country'], name = 'india'),
                        go.Scatter(x = df2['year'], y = df2['lifeExp'])
                        ])

fig.update_layout(title='Life Expectancy over the years',
                  xaxis_title = 'Years',
                  yaxis_title = 'Life Expectancy')



plot(fig)