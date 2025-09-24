import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")

def main():

    data = pd.read_csv('data.csv')
    st.write("Data Preview:")
    st.dataframe(data.head())

if __name__ == "__main__":
    main()