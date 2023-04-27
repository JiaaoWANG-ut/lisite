import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import numpy as np
import pandas as pd

# 创建 Dash 应用
app = dash.Dash(__name__)

# 定义应用布局
app.layout = html.Div([
    dcc.Graph(id='live-3d-scatter', animate=True),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)  # 更新间隔（毫秒）
])

# 回调函数，用于更新 3D 散点图
@app.callback(
    Output('live-3d-scatter', 'figure'),
    [Input('interval-component', 'n_intervals')])
def update_graph(n):
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    z = np.random.rand(N)

    df = pd.DataFrame({'x': x, 'y': y, 'z': z})

    fig = px.scatter_3d(df, x='x', y='y', z='z', color='z', size_max=10, opacity=0.7)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
