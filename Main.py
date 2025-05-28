import streamlit as st

#add color to chart
# add format stuff
# add colors to radios


st.set_page_config(
    page_title = "Budget Calculator"
)
st.title("Main Page")
st.sidebar.success("Select a page")


if 'budget' not in st.session_state: 
   st.session_state.budget = 0

if 'income' not in st.session_state: 
    st.session_state.income = 0

if 'expenses' not in st.session_state: 
    st.session_state.expenses = {"Rent": 0
    , "Utilities": 0, "Travel": 0, 
    "Food": 0, "Entertainment": 0, 
    "Subscriptions": 0, "Other": 0}

def trackBudget():
    budget_form = st.form(key = "budget_key", clear_on_submit = True, border= True)
    with budget_form: 
        st.session_state.budget = st.number_input("Enter your budget:", min_value =0, step = 10)
        submitted = st.form_submit_button("Submit") 
        if submitted: 
            st.success("Saved")

def trackIncome():

    income_form = st.form(key = "income_key", clear_on_submit = True, border= True)

    with income_form: 
        st.session_state.income  = st.number_input("Enter your income:", min_value = 0, step = 100 )

        submitted = st.form_submit_button("Submit") 
        if submitted: 
            st.success("Saved")

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
    

def displayBalance():
    st.write("Budget:", st.session_state.budget)
    # add checkmark
    st.write("Total Income:", st.session_state.income)
    st.divider()

def display():
    trackBudget()
    trackIncome()
    trackExpenses()


    sumExpenses = sum(st.session_state.expenses.values())
 
    st.write("Total Expenses:", sumExpenses)

    displayBalance()


display()



