import streamlit as st





st.set_page_config(
    page_title = "Budget Calculator"
)
st.title("Main Page")
st.sidebar.success("Select a page")


if 'income' not in st.session_state: 
    st.session_state.income = 0

if 'expenses' not in st.session_state: 
    st.session_state.expenses = {"Rent": 0
    , "Utilities": 0, "Travel": 0, 
    "Food": 0, "Entertainment": 0, 
    "Subscriptions": 0, "Other": 0}

def trackIncome():

    income_form = st.form(key = "income_key", clear_on_submit = True, border= True)

    with income_form: 
        st.session_state.income  = st.number_input("Enter your income:", min_value = 0, step = 100 )

        submitted = st.form_submit_button("Submit") 
        if submitted: 
            st.success("Saved")
        return st.session_state.income

def trackExpenses():
    expense_form = st.form(key = "expense_key", clear_on_submit = True, border= True)
    with expense_form: 
        cat = st.radio("Select a category:", list(st.session_state.expenses.keys()), index =0)
       
        # time = st.date_input("Time of purchase", max_value = "today")
        exp = st.number_input("Enter your expense:", min_value = 0, step = 1, value = st.session_state.expenses[cat] )

        st.session_state.expenses[cat] += exp 

        submitted = st.form_submit_button("Submit") 
        if submitted: 
            st.success("Saved")     
    

    # fix how its not continously updating 


def display():
    st.write("Income:", trackIncome())
    trackExpenses()

    sumExpenses = sum(st.session_state.expenses.values())
 
    st.write("Total Expenses:", sumExpenses)




display()

#implenent multip page elements if you want 


