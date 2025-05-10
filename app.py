import streamlit as st 
from langchain_groq import ChatGroq


st.title("CHAT WITH GROQ")
st.write("this is a sample app to chart with groq using langchain")
 
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)
user = st.chat_input("What do you want to ask ?")

if user:
    with st.spinner("Thinking...."):
         response = llm.invoke(user)
         st.write(response.content)
