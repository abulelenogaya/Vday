import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="wide")

# --- CSS ---
st.markdown("""
<style>
/* Remove Streamlit top padding */
.css-18e3th9 {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

/* Full-page flex to center everything vertically and horizontally */
.stApp {
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 100%);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center; /* vertical center */
    align-items: center;     /* horizontal center */
    height: 100vh;           /* full viewport height */
    margin: 0;
    padding: 0;
}

/* Heading */
.landing-heading {
    color: #b30059; /* dark pink */
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
    margin-bottom: 2rem;
    text-align: center;
    animation: fadeIn 2.5s ease-in-out;
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
div.stButton > button:hover {
    background-color: #ff5c7a !important;
    transform: scale(1.1);
    cursor: pointer;
}

/* Floating hearts animation */
@keyframes float {
    0% { transform: translateY(0px); opacity: 1; }
    50% { transform: translateY(-15px); opacity: 0.7; }
    100% { transform: translateY(0px); opacity: 1; }
}
.floating-heart {
    color: #ff5c7a;
    font-size: 2rem;
    display: inline-block;
    animation: float 3s infinite ease-in-out;
    margin: 0 5px;
}

/* Fade in for heading and subtext */
@keyframes fadeIn {
    0% {opacity:0;}
    100% {opacity:1;}
}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

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
        '<div style="text-align:center; color:#b30059; font-size:1.7rem;">'
        'So… I was going to play it cool. But that’s clearly not happening 😏 I like you ❤️'
        '</div>', unsafe_allow_html=True
    )
    if st.button("Back"):
        go_to("home")

# --- PHOTOS PAGE ---
elif st.session_state.page == "photos":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:1.7rem;">📸 Our Moments ❤️</div>',
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    col1.image("photo1.jpeg")
    col1.image("photo3.jpeg")
    col2.image("photo2.jpeg")
    col2.image("photo4.jpeg")
    if st.button("Back"):
        go_to("home")

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
