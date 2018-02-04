# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import duo2 as duo
import plotly.graph_objs as go
'''
dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker=go.Marker(
                    color='rgb(55, 83, 109)'
                )
            ),
            go.Bar(
                x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                   2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker=go.Marker(
                    color='rgb(26, 118, 255)'
                )
            )
        ],
        layout=go.Layout(
            title='US Export of Plastic Scrap',
            showlegend=True,
            legend=go.Legend(
                x=0,
                y=1.0
            ),
            margin=go.Margin(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='my-graph'
)
'''




app = dash.Dash()


df = duo.get_duo_data('Premier League')
data, layout = duo.generate_data_layout(df)
df2 = duo.get_duo_data('La Liga')
data2, layout2 = duo.generate_data_layout(df2)
df3 = duo.get_duo_data('Serie A')
data3, layout3 = duo.generate_data_layout(df3)





app.layout = html.Div(children=[
    dcc.Graph(
        figure = go.Figure(
            data = data,
            layout = layout,
            ),
    style={'height': 300,
           'margin-top':0},
    id='my-graph'
    ),

html.Div(
    dcc.Graph(
        figure = go.Figure(
            data = data2,
            layout = layout2
            ),
        style={'height': 300},
        id='my-graph2'
        ),
    style = {'align':'left',
           'margin-left':400,
           'margin-top':-300}
),

html.Div(
    dcc.Graph(
        figure = go.Figure(
            data = data3,
            layout = layout3
            ),
        style={'height': 300},
        id='my-graph3'
        ),
    style = {'align':'left',
           'margin-left':800,
           'margin-top':-300}
),
html.P('Most Productive Attacking Partnerships',
        style = {'fontFamily':'Arial',
                 'fontSize':20,
                 'fontWeight':'bold',
                 'z-index': -1,
                 'position':'relative',
                 'margin-top':-285,
                 'margin-left':60}),
html.P('Partnerships with the most chances',
        style = {'fontFamily':'Arial',
                 'fontSize':13,
                 #'fontWeight':'bold',
                 'z-index': 2,
                 'position':'relative',
                 'margin-top':-17,
                 'margin-left':60}),
html.P('@FootyNumb3rs',
        style = {'fontFamily':'Arial',
                 'color':'grey',
                 'fontSize':15,
                 #'fontWeight':'bold',
                 'z-index': 2,
                 'position':'relative',
                 'margin-top':-8.5,
                 'margin-left':1119})

],
style = {'background-color':'#f1f1f1', 'width':1300,'height':1000,'margin-top':0})



if __name__ == '__main__':
    app.run_server(debug=True)