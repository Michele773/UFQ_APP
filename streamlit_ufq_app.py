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
