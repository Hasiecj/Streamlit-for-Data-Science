#Built-in visuazizations methods

import numpy as np
import pandas as pd
import streamlit as st
 
st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"]
).reset_index()
df_dbh_grouped.columns = ["dbh", "tree_count"]
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

#Plotly visualizations
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# st.title('SF Trees')
# st.write(
#     """This app analyzes trees in San Francisco using
#     a dataset kindly provided by SF DPW"""
# )
# st.subheader('Plotly Chart')
# trees_df = pd.read_csv('trees.csv')
# fig = px.histogram(trees_df['dbh'])
# st.plotly_chart(fig)


#Matplotlib and Seaborn
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import datetime as dt
# st.title('SF Trees')
# st.write(
#     """This app analyzes trees in San Francisco using
#     a dataset kindly provided by SF DPW"""
# )
# trees_df = pd.read_csv('trees.csv')
# trees_df['age'] = (pd.to_datetime('today') -
#                    pd.to_datetime(trees_df['date'])).dt.days
# st.subheader('Seaborn Chart')
# fig_sb, ax_sb = plt.subplots()
# ax_sb = sns.histplot(trees_df['age'])
# plt.xlabel('Age (Days)')
# st.pyplot(fig_sb)
# st.subheader('Matploblib Chart')
# fig_mpl, ax_mpl = plt.subplots()
# ax_mpl = plt.hist(trees_df['age'])
# plt.xlabel('Age (Days)')
# st.pyplot(fig_mpl)

#Bokeh
# import streamlit as st
# import pandas as pd
# from bokeh.plotting import figure
# st.title('SF Trees')
# st.write('This app analyzes trees in San Francisco using'
#         ' a dataset kindly provided by SF DPW')
# st.subheader('Bokeh Chart')
# trees_df = pd.read_csv('trees.csv')
# scatterplot = figure(title = 'Bokeh Scatterplot')
# scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
# scatterplot.yaxis.axis_label = "site_order"
# scatterplot.xaxis.axis_label = "dbh"
# st.bokeh_chart(scatterplot)

#Altair

#Option 1
# import streamlit as st
# import pandas as pd
# import altair as alt
# st.title('SF Trees')
# st.write(
#     """This app analyzes trees in San Francisco using
#     a dataset kindly provided by SF DPW"""
# )
# trees_df = pd.read_csv('trees.csv')
# df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
# df_caretaker.columns = ['caretaker', 'tree_count']
# fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
# st.altair_chart(fig)

#Option 2
# import streamlit as st
# import pandas as pd
# import altair as alt
# st.title('SF Trees') 
# st.write(
#     """This app analyzes trees in San Francisco using
#     a dataset kindly provided by SF DPW"""
# )
# trees_df = pd.read_csv('trees.csv')
# fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
# st.altair_chart(fig)