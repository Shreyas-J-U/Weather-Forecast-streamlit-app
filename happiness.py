import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")

# Load data
df = pd.read_csv("happy.csv")
happy = df["happiness"]
gdp = df["gdp"]
gen = df["generosity"]

# Select data for axes
x_axis = st.selectbox("Select the data for x-axis: ",
                      ("Happiness", "GDP", "Generosity"))
y_axis = st.selectbox("Select the data for y-axis: ",
                      ("Happiness", "GDP", "Generosity"))


# Function to map selected axis to data
def get_data(x_axis, y_axis):
    if x_axis == 'Happiness':
        x_data = happy
    elif x_axis == 'GDP':
        x_data = gdp
    elif x_axis == 'Generosity':
        x_data = gen

    if y_axis == 'Happiness':
        y_data = happy
    elif y_axis == 'GDP':
        y_data = gdp
    elif y_axis == 'Generosity':
        y_data = gen

    return x_data, y_data


# Get the data for the selected axes
x_data, y_data = get_data(x_axis, y_axis)

st.subheader(f"{x_axis} vs {y_axis}")

# Create the scatter plot
figure = px.scatter(x=x_data, y=y_data, labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
