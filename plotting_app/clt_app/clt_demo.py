import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Illustrating the Central Limit Theorem with Streamlit')
st.subheader('App developed by Jakub')
st.write(('This app simulates a thousand coin flips using the chance of heads input below,'
     'and then samples with replacement from that population and plots the histogram of the'
     ' means of the samples in order to illustrate the central limit theorem!'))
perc_heads = st.number_input(label = 'Chance of Coins Landing on Heads', min_value = 0.0, max_value = 1.0, value = .5)
graph_title = st.text_input(label='Graph Title', value = "Histogram plot")
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []
for i in range(0, 1000):
     list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
# Plot the histogram on the axes object with the specified range
ax.hist(list_of_means, range=[0, 1])

# Optionally, you can set titles and labels
ax.set_title(graph_title)
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

st.pyplot(fig)
