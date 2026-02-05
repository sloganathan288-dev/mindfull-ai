import streamlit as st # type: ignore
from model import verify_news

st.set_page_config(page_title="Fake News Verification System")

st.title("📰 Fake News Detection & Verification")
st.write("This system verifies news using **multiple trusted news websites**.")

news_input = st.text_area(
    "Enter the news content:",
    height=200,
    placeholder="Paste the news article here..."
)

if st.button("Verify News"):
    if news_input.strip() == "":
        st.warning("Please enter news content.")
    else:
        with st.spinner("Searching trusted news sources..."):
            result = verify_news(news_input)
        st.success(result)
