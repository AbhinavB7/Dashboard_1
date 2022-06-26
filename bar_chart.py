
"""
Spyder Editor

@author: Abhinav Bhamidipati
"""

import plotly.graph_objects as go #create figure
import plotly.express as px #create gapminded dataset

from plotly.offline import init_notebook_mode, plot
init_notebook_mode()


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")

fig = go.Figure([go.Bar(x = df['year'], y = df['gdpPercap'], marker_color = 'green', name = 'India'),
                 go.Bar(x = df2['year'], y = df2['gdpPercap'], marker_color = 'orange')
                 ])

fig.update_layout(title = 'GDP per capita over years',
                  xaxis_title = 'yrs',
                  yaxis_title = 'GDP',
                  barmode = 'stack') #or group

plot(fig)
