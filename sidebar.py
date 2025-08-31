import streamlit as st
import pandas as pd



#Sidebar
with st.sidebar:
    st.write('Text in Side Bar')

#Columns
col1,col2,col3 = st.columns(3)
slider = col1.slider('choose a number', min_value=0.0,max_value=10.0)
col1.write(slider)

text = col2.text_area('What do you want write',placeholder='write Here')
col2.write(text)

date = col3.date_input('when am I doing this experiment?')
col2.write(date)
#Tabs
df = pd.read_csv('/Users/gmarifulislam/Desktop/code/strem1/data.csv',delimiter=';')
tab1, tab2 = st.tabs(['Line plot','Bar plot'])
with tab1:
    tab1.write('A line plot')
    st.line_chart(df, x = 'year',y = ['col1','col2','col3'] )
with tab2:
    st.write('Bar Chart')
    st.bar_chart(df, x = 'year',y = ['col1','col2','col3'] )


#Expander
with st.expander("See more"):
    st.write('You will see me, when you will expand this section')

#Container
with st.container():
    st.write('This is inside of the Container')
st.write('This is outside of the container')
