import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Create a dictionary with the data
data = {
    'Well ID': ['MW28', 'MW29', 'MW30', 'MW31', 'MW32', 'MW33', 'MW34', 'MW35', 'MW37'],
    'I2 Lab 1': [7.46, 7.29, 8.07, 6.94, 8.87, 4.5, 3.18, 7.2, 7.99],
    'Halden 1': [0.017, 0.009, 0.011, 0.023, 0.036, 0.008, 0.022, 0.006, 0.007],
    'I2 Lab 2': [2.52, 2.38, 0.003, 7.94, 2.87, 1.91, 1.76, 2.99, 10.9],
    'Halden 2': [2.13, 0.00, 0.00, 3.09, 2.53, 1.52, 1.43, 0.68, 6.04],
    'I2 Lab 3': [1.24, 0.449, 5.59, 3.07, 3.85, 0.809, 0.598, 1.99, 1.7],
    'Halden 3': [0.994, 0.491, 0.885, 0.559, 0.634, 0.688, 0.452, 1.476, 1.09],
    'I2 Lab 4': [6.43, 0.0003, 2.24, 5.19, 8.83, 4.04, 1.14, 5.84, 9.31],
    'Halden 4': [0.98, 0.00, 0.71, 1.01, 1.90, 2.10, 1.10, 1.60, 2.30]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Interactive Scatter Plot App')

# Dropdown to select the pair of I2 Lab and Halden values
pair = st.selectbox('Select the pair of I2 Lab and Halden values:', ['1', '2', '3', '4'])

# Prepare data for plotting
i2_lab_col = f'I2 Lab {pair}'
halden_col = f'Halden {pair}'

# Create the scatter plot using plotly.graph_objects
fig = go.Figure()

# Add I2 Lab data
fig.add_trace(go.Scatter(
    x=df['Well ID'],
    y=df[i2_lab_col],
    mode='markers',
    name=f'I2 Lab {pair}',
    marker=dict(color='red')
))

# Add Halden data
fig.add_trace(go.Scatter(
    x=df['Well ID'],
    y=df[halden_col],
    mode='markers',
    name=f'Halden {pair}',
    marker=dict(color='blue')
))

# Update layout
fig.update_layout(
    title=f'Scatter Plot of I2 Lab {pair} vs Halden {pair} Values',
    xaxis_title='Well ID',
    yaxis_title='Measurement',
    legend_title='Type'
)

# Show the plot in Streamlit
st.plotly_chart(fig)
