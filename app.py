import streamlit as st

# Define the sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ["Feynman's Pedagogy", 'Fine-tuning Llama 2', 'Llama2 - Feynman Model'])

# Define the content of each page
if page == "Feynman's Pedagogy":
    st.title("Feynman's Pedagogy")
    st.markdown('Richard Feynman was a brilliant physicist and an exceptional teacher. His ability to explain complex scientific concepts in an accessible and engaging way has inspired countless students and educators. His passion for science and education, combined with his unique teaching style, made his lectures a highlight for many students. Feynman’s teaching is great because he made science exciting and accessible to everyone, regardless of their background or prior knowledge.')
elif page == 'Fine-tuning Llama 2':
    st.title('Fine-tuning Llama 2 with Feynman Dataset')
    # Content for page 2 goes here
elif page == 'Llama2 - Feynman Model':
    st.title('Llama2 - Feynman Model')
    # Content for page 3 goes here