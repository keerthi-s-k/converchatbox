import streamlit as st
a=st.chat_input("enter a command")
if a:
	st.chat_message("user").write(a)
	if a.lower()=="hi":
		st.chat_message("ai").write("hello")
	elif a.lower()=="bye":
		st.chat_message("ai").write("goodbye")
	elif a.lower()=="how are you":
		st.chat_message("ai").write("im fine")
	elif a.lower()=="where do you live":
		st.chat_message("ai").write("i live in banglore")
	elif a.lower()=="what is the time":
		st.chat_message("ai").write("its 12 o'clock")
	elif a.lower()=="can i get a ticket":
		st.chat_message("ai").write("yes,here is your ticket")
	elif a.lower()=="how was your day":
		st.chat_message("ai").write("it was good")
	else:
		st.chat_message("ai").write("invalid command")
