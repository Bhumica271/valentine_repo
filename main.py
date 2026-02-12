# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 20:35:29 2026

@author: Bhumica Hooda
"""
import streamlit as st
import random

st.set_page_config(page_title="A Question From My Heart ❤️", layout="wide")

# Session state
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Romantic styling
st.markdown("""
<style>

/* Full background */
[data-testid="stAppViewContainer"] {
    background-image: url("background1.jpeg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Center card */
.card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    padding: 3.5rem;
    border-radius: 25px;
    max-width: 850px;
    margin: 5vh auto;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}

/* Heading */
.title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 3.2rem;
    color: #7a1f3d;
    margin-bottom: 0.5rem;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-style: italic;
    font-size: 1.2rem;
    color: #5a2a3c;
    margin-bottom: 2rem;
}

/* Main romantic text */
.story {
    text-align: center;
    font-family: 'Georgia', serif;
    font-size: 1.3rem;
    color: #4b2c38;
    line-height: 1.8;
    margin-bottom: 2rem;
}

/* Quote styling */
.quote {
    text-align: center;
    font-style: italic;
    font-size: 1.4rem;
    color: #6b2d4d;
    margin: 2rem 0;
}

/* Comeback */
.comeback {
    text-align: center;
    font-style: italic;
    font-size: 1.3rem;
    color: #7a1f3d;
    margin-top: 1.5rem;
}

</style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("background1.jpeg", caption="Choose well! ❤️", width=500)
# Progressive quotes
quotes = [
    "“Somewhere between hello and forever, I found my home in you.”",
    "“You are my today and all of my tomorrows.”",
    "“With you, love feels effortless.”",
    "“I didn’t just fall for you — I chose you.”",
]

# Escalating no responses
no_responses = [
    "Hmm… that doesn’t sound like your heart talking.",
    "I think you misclicked. Try again. 😌",
    "Interesting choice… but destiny disagrees.",
    "You’re persistent. I admire that.",
    "You think you can opt out? Haha… wrong. ❤️ You are bound to me for life. ❤️"
]

# YES SCREEN
if st.session_state.accepted:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>Always You ❤️</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='story'>
    Loving you feels like the most natural thing in the world. <br><br>
    If I had to choose again, in every lifetime, in every universe —  
    it would still be you.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image("Pic1.jpeg", caption="My favorite place ❤️", width=500)

    st.markdown("""
    <div class='quote'>
    “I choose you. And I’ll choose you over and over.”
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# MAIN QUESTION SCREEN
else:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<div class='title'>A Question From My Heart</div>", unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Just one question… but it means everything.</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='story'>
    From the first smile to every shared dream,  
    you’ve turned ordinary moments into something extraordinary.  
    <br><br>
    And so today, I ask you something simple…
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title' style='font-size:2.2rem;'>Will you be my Valentine?</div>", unsafe_allow_html=True)

    # Progressive quote
    if st.session_state.no_count < len(quotes):
        st.markdown(f"<div class='quote'>{quotes[st.session_state.no_count]}</div>", unsafe_allow_html=True)

    # Buttons
    col1, col2, col3 = st.columns(3)

    with col2:
        if st.button("Yes ❤️"):
            st.session_state.accepted = True
            st.rerun()

    random_col = random.choice([col1, col3])
    with random_col:
        if st.button("No"):
            st.session_state.no_count += 1

    # Escalating NO message
    if st.session_state.no_count > 0:
        msg_index = min(st.session_state.no_count - 1, len(no_responses) - 1)
        st.markdown(f"<div class='comeback'>{no_responses[msg_index]}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)






