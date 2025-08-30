import streamlit as st
import pandas as pd

with st.form('form_key'):
    st.write('🥪 Place your Subway Order')
    visit_date = st.date_input('Wchich date do you want visit?')
    visit_time = st.time_input('Which time do you want to come?')
    Bread = st.selectbox('Bread',options=['Italiyan','Seassam','Cheese Origano','Volkorn','Honey Oat'])
    size = st.selectbox('Size', options=['15cm','30cm'])
    Meat_item = st.selectbox('Meat', options=['Chicken Tariakiy', 'Legendary Tariakiy', 'Plantbase Tariakiy',
                                              'Plantbase Legendary tariakiy','Chicken Fajita','Chicken Tandoori',
                                              'Rotessarie Chicken',' Steak and Cheese','Taco Beef','Nacho Chickeen'])
    Vegitables = st.multiselect('Vegitable Items:', options=['Iceberg', 'Gurken','Tomatoo','Onion', 'Paprca',
                                                           'GäuwaGurken','Olive','Pickle', 'Rucola','Rosted Onion'])
    Sausages = st.multiselect('Which sausages would you like?', options=['Chipotle','Extra Spicy Chipotle',
                                                                         'Honey Musterd','Mayo', 'Yougurt','Ceasser','Vegan BBQ',
                                                                         'Vegan Garlic','Sweet Onion'],max_selections=3)
    Cheese = st.selectbox('Do you want to take cheese?',options=['Yes', 'No'])
    if Cheese == 'Yes':
        Cheese_type = st.selectbox('Which cheese would you like?', 
                                   options=['Cheddar', 'Scheiben Cheese',
                                            'Mozzerella EmmentalMix','Freisch Cheese', 'Mozzerella'])
    Text_Area = st.text_area('Do you have any Special request?', placeholder='Drop your request here')

    Submit_btn = st.form_submit_button('Submit')

    if Submit_btn:
        st.success("✅ Your Subway Order")
        st.write(f"Order Date {visit_date}")
        st.write(f"Order Time: {visit_time}")
        st.write(f"Bread Item: {Bread}")
        st.write(f"Size: {size}")
        st.write(f"Meat Item: {Meat_item}")
        st.write(f"Cheseese: {Cheese}")
        if Cheese == 'Yes' and Cheese_type:
            st.write(f"Cheese type: {Cheese_type}")
        st.write(f"Vegitables : {Vegitables}")
        st.write(f"Sausages: {Sausages}")
        st.write(f"Note: {Text_Area}")
        
