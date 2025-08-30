import streamlit as st
import pandas as pd

#Buttons
primary_btn = st.button(label = 'Primary',type ='primary')
secondary_btn = st.button(label='Secondary',type = 'secondary')

if primary_btn:
    st.write('Hello from Primary Button')
if secondary_btn:
    st.write('Hello from secondary button ')

#checkbox
st.divider()
checkbox = st.checkbox('I agree')

if checkbox:
    st.write('I agree with it')
else:
    st.write('I do not agree with it')


# Radio buttons
st.divider()

df = pd.read_csv('/Users/gmarifulislam/Desktop/code/strem1/data.csv',delimiter=';')

radio = st.radio('Chose a column', options = df.columns[1:],index = 0, horizontal= True)
st.write(radio)


#Select box

st.divider()
select = st.selectbox('Select a column',options=df.columns[1:],index = 0)
st.write(select)

#Multiselector
st.divider()
multi = st.multiselect('Select many columns',options=df.columns[1:],default=['col1'],max_selections= 3)
st.write(multi)
# SLider
st.divider()
slider = st.slider('pick a number',min_value=0.0, max_value=10.0) #value is the default value
st.write(slider)
#Text input
st.divider()
first_name = st.text_input('What is your first anme?', placeholder='First Name')
last_name = st.text_input('What is your last name?', placeholder='Last Name')
st.write(f" My name is {first_name} {last_name}")

# Number input

st.divider()
input_num = st.number_input('pick a number', min_value=0.0,max_value=10.0, value=0.0)
st.write(f"You have picked {input_num}")

# Text Area
st.divider()
text = st.text_area('Tell me your opinion', placeholder='Write message here')
st.write(text)