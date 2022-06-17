import streamlit as st
from string import ascii_letters, digits, punctuation
from secrets import choice
import time

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("pyRapidPassGenWEB")
st.subheader("A simple password generator using python.")

col1, col2 = st.columns(2)

with col1:
    char, number_pass, special_chars = (
        st.slider("Preferred password length?", min_value=16, max_value=50),
        st.slider("Number of passwords required?", min_value=1, max_value=25),
        st.radio("Use special characters?", ["yes", "no"]),
    )

    if st.button("Generate"):
        with st.spinner("Generating passwords..."):
            time.sleep(1)
        with col2:
            st.success("pyRapidPassGen task completed!")
            for i in range(number_pass):
                CHARACTERS = (ascii_letters, digits, punctuation)
                if special_chars == "yes":
                    x = [CHARACTERS[i] for i in [0, 1, 2]]
                    password = "".join(choice("".join(x)) for i in range(char))
                elif special_chars == "no":
                    x = [CHARACTERS[i] for i in [0, 1]]
                    password = "".join(choice("".join(x)) for i in range(char))
                st.text(password)
