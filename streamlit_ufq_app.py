# UFQ_APP Create a Prototype with Snowflake and Phyton of ufq 

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello here is the UFQ Demo Page')
streamlit.header('This is how the World is swinging')

streamlit.header('Frequences are')
streamlit.text('🥣 Planeten')
streamlit.text('🥗 Instrumente')
streamlit.text('🥑 Water')
streamlit.text('🍞 Earth')

streamlit.header('🍌🥭 Build Your Own Frequences Area 🥝(graphics like this)🍇')

# Display the table on the page.

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits from a csv file:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#create the repeatable code blocke (function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# New Section to display fruityvice api response
streamlit.header('International Astronomic free Data Frequences Advice!(This is a API Call fro fruits for testing use (apple)')
try:
  fruit_choice = streamlit.text_input('What Frequence would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a Frequence or a Fruit.")
  else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
	   
except URLerror as e:
      streamlit.error()

#import snowflake.connector

streamlit.header("View Our Fruit List - Add Your Favorites!")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from planet")
       return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

