import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=[
    dcc.Slider(
        id='k-slider',
        min=1,
        max=20,
        marks={i: '{}'.format(i) for i in range(20)},
        step=1,
        value=10,
    ),
    html.Div(id='slider-output-container-k'),
    dcc.Slider(
        id='m-slider',
        min=1,
        max=20,
        marks={i: '{}'.format(50*i) for i in range(1000)},
        step=50,
        value=400,
    ),
    html.Div(id='slider-output-container-m'),
    html.Div(children='''Probability of false positives as a function of input size'''),
    dcc.Graph(id='graph',figure=)
]
)


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)