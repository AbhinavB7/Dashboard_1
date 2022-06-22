# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:11:00 2022

@author: Abhinav Bhamidipati
"""

import plotly.express as px #create gapminded dataset
from plotly.offline import init_notebook_mode, plot
init_notebook_mode()

df = px.data.gapminder().query('year == 2007')

fig = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size = 'pop',
                 color = 'continent', hover_name = 'country',
                 log_x = True, size_max=50)


plot(fig)