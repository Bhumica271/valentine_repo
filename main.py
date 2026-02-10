# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 20:35:29 2026

@author: Bhumica Hooda
"""

import streamlit as st
import random

st.set_page_config(page_title="Be My Valentine 💘", layout="wide")

# Initialize session state
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

st.markdown(
    """
    <style>
    .center {
        text-align: center;
        font-size: 40px;
        margin-top: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="center">💖 Will you be my Valentine? 💖</div>', unsafe_allow_html=True)
st.write("")
st.write("")

col1, col2, col3 = st.columns(3)

# YES button (sweet and normal)
with col2:
    if st.button("💘 YES 💘"):
        st.balloons()
        st.success("YAY!!! 💕🥰 You just made my Valentine’s Day!")

# Random position for NO button
random_col = random.choice([col1, col3])

with random_col:
    if st.button("😅 No"):
        st.session_state.no_clicks += 1
        st.warning("Oops! That button doesn’t seem to like that answer 😉")

# Optional teasing message
if st.session_state.no_clicks > 0:
    st.markdown(
        f"<p style='text-align:center;'>You’ve tried saying no {st.session_state.no_clicks} times 😏</p>",
        unsafe_allow_html=True
    )
