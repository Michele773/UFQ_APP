# UFQ_APP Create a Prototype with Snowflake and Phyton of ufq 

import streamlit
import pandas

streamlit.title('Hallo Herwig here is the Demo Page')
streamlit.header('This is how the World is swinging')

streamlit.header('Frequences are')
streamlit.text('🥣 Planeten')
streamlit.text('🥗 Instrumente')
streamlit.text('🥑 Water')
streamlit.text('🍞 Earth')

streamlit.header('🍌🥭 Build Your Own Frequences Area 🥝🍇')

# Display the table on the page.

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
