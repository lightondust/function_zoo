import numpy as np
import plotly.express as px


def cubic_function(st):
    st.video('https://www.youtube.com/watch?v=vS0-M9SuV_s&t=4s')
    x = np.arange(-4.0, 4.0, 0.01)

    a = st.slider('a', -4.0, 4.0, step=0.01, value=1.0)
    b = st.slider('b', -4.0, 4.0, step=0.01, value=0.)
    c = st.slider('c', -4.0, 4.0, step=0.01, value=0.)
    d = st.slider('d', -4.0, 4.0, step=0.01, value=0.)
    y = a * x**3 + b * x**2 + c * x + d
    fig = px.scatter(x=x, y=y, range_x=(-4, 4), range_y=(-4, 4))
    st.plotly_chart(fig)


