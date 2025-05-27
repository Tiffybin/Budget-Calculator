import streamlit as st
import pandas as pd 



st.title("Charts")

def graphics():
    expenses = st.session_state.expenses
   
    data = pd.DataFrame({"Category": list(expenses.keys()), "Amount": list(expenses.values())})

    table = st.table(data)


    st.bar_chart(data.set_index("Category"), x_label="Category", y_label="Dollar Amount" )


graphics()