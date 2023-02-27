import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
# Load the dataset from GitHub
diamonds=sns.load_dataset("diamonds", cache=True, data_home=None)

# Define a function to display the dataframe page
def dataframe():
    st.title("Diamonds Data")
    st.header('Dataframe')
    
    # Display the dataframe
    st.write(diamonds)

# Define a function to display the overview page
def overview():
    st.title('Overview')
    
    # Display basic statistics
    st.write('Basic Statistics:')
    st.write(diamonds.describe())
    
    # Display a pairplot
    st.write('Pairplot:')
    fig = px.scatter_matrix(diamonds[['carat', 'depth', 'table', 'price']], width=800, height=800)
    st.plotly_chart(fig)
    
    # Display a correlation matrix
    st.write('Correlation Matrix:')
    fig = px.imshow(diamonds.corr())
    st.plotly_chart(fig)

# Define a function to display the scatter plot page
def scatter_plot():
    st.title('Scatter Plot')
    
    # Display the scatter plot
    fig = px.scatter(diamonds, x='carat', y='price', width=800, height=600)
    st.plotly_chart(fig)
    

# Define a function to display the histogram page
def histogram():
    st.title('Histogram')
    
    # Display the histogram
    fig = px.histogram(diamonds, x='price', nbins=20, width=800, height=600)
    st.plotly_chart(fig)

# Define a function to display the box plot page
def box_plot():
    st.title('Box Plot')
    
    # Display the box plot
    fig = px.box(diamonds, x='cut', y='price', width=800, height=600)
    st.plotly_chart(fig)

# Add a navigation menu to switch between pages
menu = ['Dataframe', 'Overview', 'Scatter Plot', 'Histogram', 'Box Plot']
choice = st.sidebar.selectbox('Select a page', menu)

# Show the appropriate page based on the menu choice
if choice == 'Overview':
    overview()
elif choice == 'Dataframe':
    dataframe()
elif choice == 'Scatter Plot':
    scatter_plot()
elif choice == 'Histogram':
    histogram()
elif choice == 'Box Plot':
    box_plot()
