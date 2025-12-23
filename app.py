import streamlit as st
import requests
import json

st.set_page_config(page_title="GenAI Error Explainer", page_icon="🤖")

st.title("🤖 GenAI Code Error Explainer (Python)")
st.write("Uses a local LLM to explain code errors in simple English.")

error_message = st.text_area(
    "Paste your code error:",
    height=200,
    placeholder="Example: TypeError: can only concatenate str (not \"int\") to str"
)

if st.button("Explain using AI"):
    if error_message.strip() == "":
        st.warning("Please paste an error message.")
    else:
        with st.spinner("AI is thinking..."):
            prompt = f"""
Explain this programming error in very simple English.

Give:
1. Meaning
2. Why it happens
3. How to fix it
4. Simple example

Error:
{error_message}
"""

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )

            result = response.json()
            st.subheader("🧠 AI Explanation")
            st.write(result["response"])
