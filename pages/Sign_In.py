import streamlit as st
import mysql.connector
from streamlit_extras.switch_page_button import switch_page
#from Notler import SESSION
from session import SESSION

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin',
    database='notler'
)
cursor = db.cursor(dictionary=True)

st.title("Sign In")

if SESSION['loggedin'] == False:
    username = st.text_input("Username")
    password = st.text_input("Password")

    if(st.button("Sign In")):
        cursor.execute(f"select * from account where username = %s", (username, ))
        user = cursor.fetchone()
        try:
            if user['password'] == password:
                SESSION['loggedin'] = True
                SESSION['username'] = username
                st.success("Logged In I guess?")
                switch_page("home_page")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.write("Don't have an account")
    if st.button("Sign Up"):
        switch_page("Sign_Up")
else:
    switch_page("home_page")