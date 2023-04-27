import plotly.graph_objs as go
import plotly.offline as offline
import numpy as np

# 定义晶格矢量
a = 1.0
lattice = np.array([
    [a, 0.0, 0.0],
    [0.0, a, 0.0],
    [0.0, 0.0, a],
])


A=lattice
# 定义晶格中的一些点
points = [
    (0.0, 0.0, 0.0),
    (0.5, 0.5, 0.5),
    (0.5, 0.0, 0.0),
    (0.0, 0.5, 0.0),
    (0.0, 0.0, 0.5),
]

# 定义立方体盒子的顶点
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# 定义立方体盒子的边
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# 绘制立方体盒子及其边
fig = go.Figure()
fig.add_trace(go.Mesh3d(x=x, y=y, z=z, color='black', opacity=0.1))

for edge in edges:
    x0, y0, z0 = A @ np.array([x[edge[0]], y[edge[0]], z[edge[0]]])
    x1, y1, z1 = A @ np.array([x[edge[1]], y[edge[1]], z[edge[1]]])
    fig.add_trace(go.Scatter3d(x=[x0, x1], y=[y0, y1], z=[z0, z1], mode='lines', line=dict(color='black', width=5)))



for point in points:
    data.append(go.Scatter3d(x=[point[0]],
                             y=[point[1]],
                             z=[point[2]],
                             mode='markers',
                             marker=dict(color='blue', size=10)))

# 创建布局
layout = go.Layout(scene=dict(xaxis=dict(title='X'),
                              yaxis=dict(title='Y'),
                              zaxis=dict(title='Z')),
                   margin=dict(l=0, r=0, b=0, t=0))

# 创建图形对象
fig = go.Figure(data=data, layout=layout)

# 保存图形为 HTML 文件
offline.plot(fig, filename='lattice.html', auto_open=True)
