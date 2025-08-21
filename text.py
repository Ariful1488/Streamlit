import streamlit as st



#give App litile
st.title('This is The Title of Straemlit App')
#Header
st.header('Here, you are looking the main Header')

#Subheader
st.subheader('You are lookin the sub Header Part')
#Markdown
st.markdown('This is example of markdown by using markdown key word and **Double Star sign**')
# one # sign indicates Header 1
st.markdown('# one hash sign indicateds the Header 1')
#Two hash sign indicates subheader1
st.markdown('## Two hash sign indicateds the Header 2')
# How many you will give hash, it will decrese the header size
st.markdown('### Thre hash make´s more smaller than two hash')

#Caption
st.caption('I can create caption from here ')
#Code block
st.code('''
import pandas as pd
df = pd.read_csv(My_csv)

''')
#Preformatted Text
st.text('This is a simple text')

#Latex
st.latex(' x = 2^2')

#Divider
st.text('The text divider is bellow')
st.divider()
st.text('The text divider is above')

#st.write
st.write(' you wite by st.write function')