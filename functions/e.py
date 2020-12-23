import numpy as np
import plotly.express as px


def e(st):
    x = np.arange(1., 31., 1.)
    x = x ** 2
    max = st.slider('value to', 1, 30, 1)
    x = x[:max]
    fig = px.line(x=x, y=(1+1/x)**x)
    st.plotly_chart(fig)
