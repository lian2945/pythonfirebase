import streamlit as st
st.title("How to use Streamlit :confounded:")
st.header("1. Write and magic")
st.divider()
st.subheader("st.write()")
code='''st.write("Hello world!")'''
st.text("Code")
st.code(code, language="python")
st.text_area(label="Result", value="Hello World!")