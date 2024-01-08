import streamlit as st
import mysql.connector
from streamlit_extras.switch_page_button import switch_page
from session import SESSION

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin',
    database='notler'
)
cursor = db.cursor(dictionary=True)

st.title("Sign Up")

if SESSION['loggedin'] == False:
    username = st.text_input("Username")
    email = st.text_input("Email ID")
    password = st.text_input("Password")

    if(st.button("Sign Up")):
        try:
            cursor.execute("select * from account where username = %s", (username, ))
            account = cursor.fetchone()
            if account: 
                st.error("Account Already Exists Try signing in")
                st.toast("Account Already Exists")
            else:
                cursor.execute(f"insert into account values(%s,%s,%s)", (username, email, password, ))
                db.commit()
                st.success("Account Created Sucessfully")
                st.toast("Account Created Sucessfully")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.write("Already have an account")
    if st.button("Sign In"):
        switch_page("Sign_In")
else:
    switch_page("Home_Page")