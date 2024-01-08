import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from session import SESSION

if SESSION["loggedin"]:
    switch_page("Home_Page")
    st.rerun()
else:
    st.title("Notler")

    if st.button("Sign In"):
        try:
            switch_page("sign_in")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    if st.button("Sign Up"):
        try:
            switch_page("sign_up")
        except Exception as e:
            st.error(f"Error: {str(e)}")