import streamlit as st
from functions.cubic import cubic_function
# from functions.sin_over_x import sin_over_x
from functions.e import e


function = st.selectbox('chose a function view', ['cubic', 'e'])

if function == 'cubic':
    cubic_function(st)

elif function == 'e':
    e(st)
