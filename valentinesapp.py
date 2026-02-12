import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="wide")

# --- CSS ---
st.markdown("""
<style>
/* Remove default top padding */
.css-18e3th9 {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Full-page gradient background */
.stApp {
    font-family: 'Comic Sans MS', cursive, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    margin: 0;
    padding: 0;
    min-height: 100vh;

    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 30%, #ffb6c1 60%, #ff8da4 100%);
}

/* Remove white container background and adjust vertical centering */
.block-container {
    background-color: transparent;
    padding-top: 25vh;
    padding-bottom: 5vh;
}

/* Heading */
.landing-heading {
    color: #b30059;
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 1rem;
    text-align: center;
    animation: fadeIn 2s ease-in-out;
}

/* Subtext */
.landing-subtext {
    color: #b30059;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 4rem;
    text-align: center;
    animation: fadeIn 2.5s ease-in-out;
}

/* Floating emojis in heading/subtext */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}
.floating-heart {
    color: #ff5c7a;
    font-size: 2rem;
    display: inline-block;
    animation: float 3s infinite ease-in-out;
    margin: 0 5px;
}

/* Buttons */
div.stButton > button {
    border-radius: 20px !important;
    padding: 1.2rem 2.5rem !important;
    font-size: 1.5rem !important;
    font-weight: 700;
    background-color: #ff8da4 !important;
    color: #fff !important;
    margin: 0 10px !important;
    transition: transform 0.3s, background-color 0.3s;
}

/* Hover + pulse */
div.stButton > button:hover {
    background-color: #ff5c7a !important;
    transform: scale(1.1);
    animation: pulse 1s infinite;
    cursor: pointer;
}

/* Pulse animation */
@keyframes pulse {
    0% { transform: scale(1.1); }
    50% { transform: scale(1.15); }
    100% { transform: scale(1.1); }
}

/* Fade in */
@keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}

/* Fade in sequential for paragraphs */
.fade-part {
    opacity: 0;
    animation: fadeIn 1.5s forwards;
}
.fade-part:nth-child(1) { animation-delay: 0.5s; }
.fade-part:nth-child(2) { animation-delay: 1.5s; }
.fade-part:nth-child(3) { animation-delay: 2.5s; }
.fade-part:nth-child(4) { animation-delay: 3.5s; }
.fade-part:nth-child(5) { animation-delay: 4.5s; }
.fade-part:nth-child(6) { animation-delay: 5.5s; }
.fade-part:nth-child(7) { animation-delay: 6.5s; }
.fade-part:nth-child(8) { animation-delay: 7.5s; }
.fade-part:nth-child(9) { animation-delay: 8.5s; }
.fade-part:nth-child(10) { animation-delay: 9.5s; }

/* Carousel image fade and size */
.carousel-image {
    transition: opacity 1s ease-in-out;
    max-height: 70vh; /* fit screen height */
    object-fit: contain;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "photo_index" not in st.session_state:
    st.session_state.photo_index = 0

def go_to(page):
    st.session_state.page = page

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.markdown(
        '<div class="landing-heading">Hey you <span class="floating-heart">❤️</span><span class="floating-heart">💖</span></div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="landing-subtext">Open this… if you dare 😏</div>', unsafe_allow_html=True)

    # Horizontal buttons
    col1, col2, col3, col4 = st.columns([1,1,1,1], gap="medium")
    if col1.button("💌 A Message"):
        go_to("message")
    if col2.button("🎵 My Song for You"):
        go_to("song")
    if col3.button("📸 Our Moments"):
        go_to("photos")
    if col4.button("✨ Something Extra"):
        go_to("extra")

# --- MESSAGE PAGE ---
elif st.session_state.page == "message":
    st.markdown(
        """
        <div style="text-align:center; color:#b30059; font-size:1.6rem; line-height:1.5;">
            <p class="fade-part">So… I was going to play it cool.</p>
            <p class="fade-part">But that’s clearly not happening 😏</p>
            <p class="fade-part">I like you. And not in a subtle way.<br>In a “catching myself smiling at my phone” kind of way.</p>
            <p class="fade-part">You've been on my mind a little more than I'd like to admit. (Don't let it get to your head lol..)</p>
            <p class="fade-part">I like our little moments. The way our conversations shift from playful to… something else.<br>The tension. The ease. The way it feels exciting but natural.</p>
            <p class="fade-part">Just know… I’m very aware of the effect you have on me.</p>
            <p class="fade-part">And I don’t hate it. ❤️</p>
            <p class="fade-part">This is still new, and I think that's my favorite part. We're still discovering each other.<br>Still learning the details. Still choosing to lean in. And I just want you to know that I've been really enjoying it.<br>Enjoying you.</p>
            <p class="fade-part">I don't know exactly where this goes yet. But I know that right now, I'm grateful it's you I'm getting to explore this with.</p>
            <p class="fade-part">And that feels special to me. ❤️</p>
        </div>
        """, unsafe_allow_html=True
    )
    if st.button("Back"):
        go_to("home")

# --- PHOTOS PAGE (Carousel) ---
elif st.session_state.page == "photos":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:1.7rem; margin-bottom:1rem;">📸 Our Moments ❤️</div>',
        unsafe_allow_html=True
    )

    # List of photos and captions
    photos = [
        ("photo1.jpeg", "First cute moment"),
        ("photo2.jpeg", "Our silly faces"),
        ("photo3.jpeg", "Memories together"),
        ("photo4.jpeg", "Funny times ❤️")
    ]
    current_photo, caption = photos[st.session_state.photo_index]

    st.image(current_photo, use_column_width=True, caption=caption, output_format="auto")

    col1, col2, col3 = st.columns([1,1,1])
    if col1.button("Previous"):
        st.session_state.photo_index = (st.session_state.photo_index - 1) % len(photos)
    if col2.button("Back"):
        go_to("home")
    if col3.button("Next"):
        st.session_state.photo_index = (st.session_state.photo_index + 1) % len(photos)

# --- SONG PAGE ---
elif st.session_state.page == "song":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:1.7rem;">🎵 My Song for You… reminds me of you ❤️</div>',
        unsafe_allow_html=True
    )
    if st.button("Back"):
        go_to("home")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:1.7rem;">✨ Don’t Press This… 😏</div>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    if col1.button("Do Not Press 😏"):
        col1.image("funny.jpeg")
    if st.button("Back"):
        go_to("home")
