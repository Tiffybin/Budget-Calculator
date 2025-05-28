import streamlit as st
import pandas as pd 
import altair as alt 



st.title("Charts")
st.sidebar.success("Select a page")

def graphics():
    expenses = st.session_state.expenses
   
    data = pd.DataFrame({"Category": list(expenses.keys()), "Amount": list(expenses.values())})

    st.table(data)



    colors = ["#fc2003", "#595552","#056af7", "#f79605", "#52f705", "#ed2bda", "#963bdb" ]
    color_scale = alt.Scale(domain= data["Category"].tolist(), range = colors)
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X("Category", title="Category"),
        y=alt.Y("Amount", title="Dollar Amount ($)"),
        color=alt.Color("Category", scale=color_scale, legend=None)
    ).properties(width=600, height=400)

    st.altair_chart(chart, use_container_width=True)

graphics()