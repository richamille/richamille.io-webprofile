from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Richamille's Web Profile", page_icon=":ribbon:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/a1136a30-c9a8-4172-ad57-323a41d8556d/OxE3IwqGxz.json")
lottie_msg = load_lottieurl("https://lottie.host/a8e4a2e8-867b-45ab-82a5-fffb85a93b39/XJZ09tXsnW.json")
lottie_hello = load_lottieurl("https://lottie.host/fd206f87-3bc2-4e0e-8daa-69609bc94684/baT5OzUbFT.json")
img_taskhive = Image.open("images/taskhive.png")
img_brewscape = Image.open("images/brewscape.png")
img_pawsome = Image.open("images/pawsome.png")


# ---- USER LOGIN ----
def login():
    st.write("## Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        response = requests.post("https://your-api-url/login", json={"username": username, "password": password})
        if response.status_code == 200:
            user_data = response.json()
            st.session_state.user = user_data  # Store user data in session state
            st.success("Login successful!")
        else:
            st.error("Login failed. Please check your credentials.")

if 'user' not in st.session_state:
    login()
else:
    st.write(f"Welcome, {st.session_state.user['name']}!")

with st.container():
    nyan_column, text_column = st.columns((1, 2))
    with nyan_column:
        st_lottie(lottie_hello, height=400,key="hello")
    with text_column:
        st.subheader("Welcome to my profile~ :ribbon:")
        st.title("Hi, I am Richamille! :purple_heart:")
        st.write("In a world of fast-paced technology, I want to learn where I can stand in this development and how I can not only maintain but also succeed from stance through creative innovation. ")
        st.write("[Learn More >](https://richamille.github.io/richamilleadaro.github.io/)") 

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.header("Who Am I")
        # st.write("##")
        st.write(
            """
            - Richamille L. Adaro
            - December 5, 2003
            - BSIT Student
            - Davao del Norte State College
            
            """
        )

    with left_column:
        st.header("What I do")
        st.write(
            """
            - Coding
            - Graphic Design
            - Painting
            """
        )
    with middle_column:
        st.header("I've worked on")
        st.write(
            """
            - Java
            - PHP
            - Laravel
            - HTML, CSS, Javascript
            """
        )
    with middle_column:
        st.header("Currently Interested In")
        # st.write("##")
        st.write(
            """
            - Web Development
            - Python
            - Angular JS
            
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=500,key="coding")

#----  PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1.5, 1))
    with image_column:
        st.image(img_taskhive)
    with text_column:
        st.subheader("TaskHive")
        st.write(
            """
            - JAVA
            - A task tracker system 
            - "Where tasks swarm together and productivity thrive."

            """
        )
        st.markdown("[Learn More >](https://richamille.github.io/richamilleadaro.github.io/taskhive.html)")
    st.write("##")
with st.container():
    image_column, text_column = st.columns((1.5, 1))
    with image_column:
        st.image(img_brewscape)
    with text_column:
        st.subheader("Brewscape")
        st.write(
            """
            - HTML, CSS, JAVASCRIPT
            - A website for a cafe 
            - "A sensory escape, one sip at a time."
            """
        )
        st.markdown("[Learn More >](https://richamille.github.io/richamilleadaro.github.io/brewscape.html)")
    st.write("##")
with st.container():
    image_column, text_column = st.columns((1.5, 1))
    with image_column:
        st.image(img_pawsome)
    with text_column:
        st.subheader("Customer Service Ticketing System")
        st.write(
            """
            - PHP, LARAVEL, HTML, CSS, JAVASCRIPT
            - A customer service department extension website of the Pawsome Company 
            - "Experience Pawsome in Customer Service."
            """
        )
        st.markdown("[Learn More >](https://richamille.github.io/richamilleadaro.github.io/pawsome.html)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me! :ribbon:")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/richamillea@gmail.com" method="POST">
        <inout type="hidden" name="_captcha+ value="false">
        <input type="text" name="name" placeholder ="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
          st_lottie(lottie_msg, height=350,key="msg")

    