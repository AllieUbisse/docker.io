import streamlit as st

# Set the title of the app
st.title('Basic Streamlit App')

# Create a sidebar with a slider
st.sidebar.header('User Input')
number = st.sidebar.slider('Select a number', 0, 100, 50)

# Display the selected number
st.write(f'Selected number: {number}')

# Add a simple plot
st.subheader('Simple Plot')
st.line_chart([1, 2, 3, number, 5, 6])
