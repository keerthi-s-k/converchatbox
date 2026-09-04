import streamlit as st
a=st.chat_input("enter hi/bye")
if a:
	st.chat_message("user").write(a)
	if a.lower()=="hi":
		st.chat_message("ai").write("hello")
	elif a.lower()=="bye":
		st.chat_message("ai").write("goodbye")
