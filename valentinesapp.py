#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 20:36:11 2026

@author: abulelenogaya
"""

import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #FFF5F7;
    font-family: 'Helvetica', sans-serif;
    position: relative;
    overflow: hidden;
}

/* Floating hearts */
@keyframes floatUp {
    0% {transform: translateY(0px); opacity:1;}
    100% {transform: translateY(-800px); opacity:0;}
}
.heart {
    position: absolute;
    font-size: 2rem;
    animation: floatUp 8s linear infinite;
    opacity: 0;
}
.heart:nth-child(1) { left: 10%; animation-delay: 0s; }
.heart:nth-child(2) { left: 30%; animation-delay: 2s; }
.heart:nth-child(3) { left: 50%; animation-delay: 4s; }
.heart:nth-child(4) { left: 70%; animation-delay: 1s; }
.heart:nth-child(5) { left: 90%; animation-delay: 3s; }

/* Cards */
.card {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
    animation: fadeIn 1s ease forwards;
}

/* Fade-in animation */
@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

/* Center */
.center { text-align: center; }

/* Buttons */
button {
    border-radius: 12px !important;
    padding: 0.8rem 1.5rem !important;
    font-size: 1.1rem;
    transition: transform 0.2s;
}
button:hover {
    transform: scale(1.05);
    cursor: pointer;
}
</style>

<!-- Floating hearts HTML -->
<div class="heart">❤️</div>
<div class="heart">❤️</div>
<div class="heart">❤️</div>
<div class="heart">❤️</div>
<div class="heart">❤️</div>
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
    st.markdown("## Happy Valentine's Day Sthandwa Sam ❤️")
    st.markdown("I made something for you... I think you'll like it 😏")
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

And that feels special to me.

❤️
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
    st.markdown("This one reminds me of you... ❤️ It says - you are my smile. you are my love.")

    # Replace YOUR_TRACK_ID with your Spotify link
    st.markdown("""
<iframe style="border-radius:12px" 
src="https://open.spotify.com/embed/track/https://open.spotify.com/track/69qJqxCXyZhaVjgqZEzrdq" 
width="100%" height="152" frameBorder="0" allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
""", unsafe_allow_html=True)

    if st.button("Back"):
        go_to("menu")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown("## ✨ Don’t Press This…")

    if st.button("Do Not Press 👀"):
        st.image("funny.jpeg", caption="What that tongue do? 😛")
        st.markdown("Haha, you're too cute! 😍")

    if st.button("Back"):
        go_to("menu")
