import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 


st.title("Charts")

def graphics():
    expenses = st.session_state.expenses
   
    data = pd.DataFrame({"Category": list(expenses.keys()), "Amount": list(expenses.values())})

    table = st.table(data)


    plt.show()

    st.bar_chart(data.set_index("Category"), x_label="Category", y_label="Dollar Amount" )


graphics()