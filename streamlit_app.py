import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header('st.write')

st.header('display text')
st.write("*hello banana bus squad* :sunglasses:")

st.header('display numbers')
st.write(1234)

st.header('display dataframe')
df=pd.DataFrame({
    'first column': [1,2,3,4,],
    'second column': [10,20,30,40]
})
st.write(df)

st.write('below is a dataframe',df,'above is a dataframe')

st.header('display charts')
df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)
st.write(c)