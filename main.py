import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.header("TEST DEPLOYMENT")

llm = ChatOpenAI(openai_api_key=os.environ["OPENAI_API_KEY"])
st.write(llm.invoke("Write a Chuck Norris joke."))



