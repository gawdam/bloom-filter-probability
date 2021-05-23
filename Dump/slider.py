import numpy as np
import plotly.graph_objects as go
import math
import chart_studio
username = "Gowdamn"
api_key = "GUrcvT3BxNuabS7JdcZz"
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

bitarray_size_max = 500
hash_function_max = 40
array_size_max = 100
# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for k in np.arange(2, hash_function_max, 2):
    for m in np.arange(5, bitarray_size_max, 5):
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#00CED1", width=6),
                name="Hash functions = " + str(k) + "| Bitarray Size = "+str(m),
                x=np.arange(1, array_size_max, 1),
                y=[pow(1 - math.exp(-k / (m / x)), k) for x in np.arange(1, array_size_max, 1)]))

# Make 10th trace visible
fig.data[10].visible = True
# Create and add slider
bitarray_sizes = []
hash_functions = []
for k in range(2, hash_function_max, 2):
    step2 = dict(
        method="update",
        args=[{"visible": [False] * hash_function_max * bitarray_size_max},
              {"title": "False-positive probability p as a function of n, {}, {}".format(k, m)}],  # layout attribute
    )
    step2["args"][0]["visible"][int((k / 2 - 1) * 100 + m / 5 - 1)] = True  # Toggle i'th trace to "visible"
    bitarray_sizes.append(step2)

    for m in range(5, bitarray_size_max, 5):
        step = dict(
            method="update",
            args=[{"visible": [False] * bitarray_size_max * hash_function_max},
                  {"title": "False-positive probability p as a function of n, {}, {}".format(k,m)}],  # layout attribute
        )
        step["args"][0]["visible"][int((k/2-1)*100+m/5-1)] = True  # Toggle i'th trace to "visible"
        hash_functions.append(step)


# for m in range(5, bitarray_size_max, 5):
#     step2 = dict(
#         method="update",
#         args=[{"visible": [False] * bitarray_size_max*hash_function_max},
#               {"title": "False-positive probability p as a function of n, {}, {}".format(k,m)}],  # layout attribute
#     )
#     step2["args"][0]["visible"][int((k/2-1)*100+m/5-1)] = True  # Toggle i'th trace to "visible"
#     bitarray_sizes.append(step2)

sliders = [dict(
    active=2,
    currentvalue={"prefix": "Hash Functions: "},
    pad={"t": hash_function_max},
    steps=hash_functions
),
    dict(
        active=55,
        currentvalue={"prefix": "Bitarray Size: "},
        pad={"t": bitarray_size_max},
        steps=bitarray_sizes
    )
]

fig.update_layout(
    sliders=sliders
)

fig.show()

py.plot(fig)
