import streamlit as st

st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="wide")

# --- CSS for animations ---
st.markdown("""
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 100%);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    text-align: center;
}

/* Heading */
h1 {
    color: #b30059;
    font-size: 3rem;
    font-weight: 900;
    animation: fadeIn 2s ease-in-out;
}

/* Subtext */
h3 {
    color: #b30059;
    font-size: 2rem;
    font-weight: 700;
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
    margin: 10px !important;
    transition: transform 0.3s, background-color 0.3s;
}
div.stButton > button:hover {
    background-color: #ff5c7a !important;
    transform: scale(1.1);
    cursor: pointer;
}

/* Floating hearts */
@keyframes float {
    0% { transform: translateY(0px); opacity: 1; }
    50% { transform: translateY(-20px); opacity: 0.7; }
    100% { transform: translateY(0px); opacity: 1; }
}

.floating-heart {
    color: #ff5c7a;
    font-size: 2rem;
    display: inline-block;
    animation: float 3s infinite ease-in-out;
    margin: 0 5px;
}

/* Fade in animation for text */
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
    st.markdown('<h1>Hey you <span class="floating-heart">❤️</span><span class="floating-heart">💖</span><span class="floating-heart">💘</span></h1>', unsafe_allow_html=True)
    st.markdown('<h3>Open this… if you dare 😏</h3>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
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
    st.markdown("<h3>So… I was going to play it cool. But that’s clearly not happening 😏 I like you ❤️</h3>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")

# --- PHOTOS PAGE ---
elif st.session_state.page == "photos":
    st.markdown("<h3>📸 Our Moments ❤️</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.image("photo1.jpeg")
    col1.image("photo3.jpeg")
    col2.image("photo2.jpeg")
    col2.image("photo4.jpeg")
    if st.button("Back"):
        go_to("home")

# --- SONG PAGE ---
elif st.session_state.page == "song":
    st.markdown("<h3>🎵 My Song for You… reminds me of you ❤️</h3>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown("<h3>✨ Don’t Press This… 😏</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    if col1.button("Do Not Press 😏"):
        col1.image("funny.jpeg")
    if st.button("Back"):
        go_to("home")
