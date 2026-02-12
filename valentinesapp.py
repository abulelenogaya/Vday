#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 21:52:21 2026

@author: abulelenogaya
"""

import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")

# --- Soft Pink Theme & Decorative Hearts ---
st.markdown("""
<style>
/* Background soft pink gradient */
.stApp {
    background: linear-gradient(135deg, #ffe6f0 0%, #fff0f5 100%);
    font-family: 'Helvetica', sans-serif;
}

/* Card styling */
.card {
    background-color: #ffffffcc;  /* slightly transparent white */
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 6px 25px rgba(255, 182, 193, 0.2); /* soft pink shadow */
    margin-bottom: 1.5rem;
}

/* Center alignment */
.center { text-align: center; }

/* Buttons styling */
button {
    border-radius: 12px !important;
    padding: 0.8rem 1.5rem !important;
    font-size: 1.1rem;
    transition: transform 0.2s;
    background-color: #ffc0cb;  /* soft pink */
    border: none;
    color: #fff;
}
button:hover {
    transform: scale(1.05);
    cursor: pointer;
    background-color: #ffb6c1;  /* slightly darker pink on hover */
}
</style>

<!-- Decorative hearts -->
<div class='center'>
💖 💕 💗 💖 💕 💗 💖  
</div>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Navigation Function ---
def go_to(page_name):
    st.session_state.page = page_name

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.markdown("<div class='card center'>", unsafe_allow_html=True)
    st.markdown("## Hey you ❤️")
    st.markdown("Open this… if you dare 😏")
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Open 💕"):
        go_to("menu")

    st.markdown("</div>", unsafe_allow_html=True)

# --- MENU PAGE ---
elif st.session_state.page == "menu":
    st.markdown("<div class='center'>", unsafe_allow_html=True)
    st.markdown("## Choose something 💌")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💌 A Message"):
            go_to("message")
        if st.button("🎵 My Song for You"):
            go_to("song")

    with col2:
        if st.button("📸 Our Moments"):
            go_to("photos")
        if st.button("✨ Something Extra"):
            go_to("extra")

    st.markdown("</div>", unsafe_allow_html=True)

# --- MESSAGE PAGE ---
elif st.session_state.page == "message":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 💌 For You")

    st.markdown("""
So… I was going to play it cool.  

But that’s clearly not happening 😏  

I like you. And not in a subtle way.  
In a “catching myself smiling at my phone” kind of way.  

You've been on my mind a little more than I'd like to admit. (Don't let it get to your head lol..)

I like our little moments. The way our conversations shift from playful to… something else.  
The tension. The ease. The way it feels exciting but natural.  

Just know… I’m very aware of the effect you have on me.  

And I don’t hate it. ❤️

This is still new, and I think that's my favorite part. We're still discovering each other.
Still learning the details. Still choosing to lean in. And I just want you to know that I've been really enjoying it.
Enjoying you.

I don't know exactly where this goes yet. But I know that right now, I'm grateful it's you I'm getting to explore this with.

And that feels special to me.❤️
""")

    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("menu")

# --- PHOTOS PAGE ---
elif st.session_state.page == "photos":
    st.markdown("## 📸 Our Moments")
    st.markdown("Little memories, just for us.")

    col1, col2 = st.columns(2)

    with col1:
        st.image("photo1.jpeg", caption="I still can't believe I cried like this after the first link 🤭")
        st.image("photo2.jpeg", caption="We look a little too cute here ❤️")

    with col2:
        st.image("photo3.jpeg", caption="I always have fun with you🫶")
        st.image("photo4.jpeg", caption="My main character😘")

    if st.button("Back"):
        go_to("menu")

# --- SONG PAGE ---
elif st.session_state.page == "song":
    st.markdown("## 🎵 My Song for You")
    st.markdown("This one reminds me of you... ❤️ ")
    st.markdown(""" It says - you are my smile. you are my love. 🥺💕

""")

    if st.button("Back"):
        go_to("menu")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown("## ✨ Don’t Press This…")

    if st.button("Do Not Press 😏"):
        st.image("funny.jpeg", caption="What that tongue do? 😛")
        st.markdown("Haha, you're too cute! 😍")

    if st.button("Back"):
        go_to("menu")
