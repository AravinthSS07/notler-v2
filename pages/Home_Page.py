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

if SESSION['loggedin']:
    st.title("Your Notes")
    st.sidebar.title(f"Username: {SESSION['username']}")
    if st.sidebar.button("Sign Out"):
        SESSION['loggedin'] = False
        switch_page("notler")
        st.rerun()
    username = SESSION['username']
    cursor.execute("select * from newnote where username = %s", (username, ))
    notes = cursor.fetchall()
    newnote = st.text_input("Enter New Note")
    if st.button("Add Note"):
        cursor.execute("insert into newnote(username, note) values(%s,%s)", (username, newnote, ))
        db.commit()
        st.rerun()
    for i in notes:
        viewnote = st.chat_message("user")
        viewnote.write(i['note'])
        if viewnote.button("Delete Note", key=i['noteid']):
            cursor.execute(f"delete from newnote where noteid = {i['noteid']}")
            db.commit()
            st.rerun()
else:
    st.error("Please Login in First")
    if st.button("Sign In"):
        switch_page("Sign_In")