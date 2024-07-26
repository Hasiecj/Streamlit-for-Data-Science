import altair as alt
import pandas as pd
import seaborn as sns
import streamlit as st
import os
import time

# os.chdir("./penguin_app")

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

#import our data
# penguins_df = pd.read_csv('penguins.csv')

#Columns of our interest
#penguins_df.columns[2:6]

penguin_file = st.file_uploader(
    'Select Your Local Penguins CSV (default provided)')

@st.cache_data()
def load_file(penguin_file):
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return(df)
penguins_df = load_file(penguin_file)

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}

# selected_species = st.selectbox('What species would you like to visualize?',
#      penguins_df['species'].unique())
selected_x_var = st.selectbox('What do you want the x variable to be?',
     penguins_df.columns[2:6])
selected_y_var = st.selectbox('What about the y?',
     penguins_df.columns[2:6])

selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male penguins', 'female penguins'])
if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

# penguins_df = penguins_df[penguins_df['species'] == selected_species] 

alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
