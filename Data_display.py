import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/gmarifulislam/Desktop/code/strem1/data.csv',delimiter=';')

st.dataframe(df)
st.write(df)
st.table(df)

#We can add matric
st.metric(label='Popularion',value =900,delta=20, delta_color='normal')


# Streamlit line chart
st.line_chart(df, x = 'year', y = ['col1','col2','col3'])

# Streamlit Area chart
st.area_chart(df,x ='year', y = ['col1','col2','col3'] )
#Streamlit bar chart
st.bar_chart(df,x = 'year', y = ['col1','col2','col3'])
#Streamlit map
geo_df = pd.read_csv('/Users/gmarifulislam/Desktop/code/strem1/sample_map.csv')
st.map(geo_df )

#Streamlit matplotlib
fig, ax = plt.subplots(1,2, figsize =(10,8))
ax[0].plot(df.year, df.col1)
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Values')

ax[1].plot(df.year, df.col2)
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Values of y')

fig.suptitle('This is a matplotlib figure')
fig.autofmt_xdate()

st.pyplot(fig)