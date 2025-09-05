import streamlit as st
import time
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


st.title('About Caching')

st.button('Test Cache')

st.subheader('st.cache_data')
@st.cache_data
def cach_run():
    time.sleep(2)
    out = 'I have done the running'
    return out
out = cach_run()
st.write(out)

st.subheader('st.cache_resource')

@st.cache_resource
def simple_linear_model():
    time.sleep(2)
    x = np.array([1,2,3,4,5,6]).reshape(-1,1)
    y = np.array([1,2,3,4,5,6])

    model = LinearRegression().fit(x,y)
    return model

lr = simple_linear_model()
x_pred = np.array([8]).reshape(-1,1)
pred = lr.predict(x_pred)
st.write(f"The prediction is {pred[0]}")
