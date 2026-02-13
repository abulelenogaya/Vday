import streamlit as st

st.set_page_config(page_title="For You", page_icon="💌", layout="wide")

# --- CSS ---
st.markdown("""
<style>
/* Remove top padding */
.css-18e3th9 {padding-top:0rem; padding-bottom:0rem;}
.stApp {
    font-family: 'Comic Sans MS', cursive, sans-serif; 
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 30%, #ffb6c1 60%, #ff8da4 100%);
    position: relative;
    overflow: hidden;
}

/* Floating hearts animation */
.heart {
    position: fixed;
    font-size: 2rem;
    opacity: 0.6;
    animation: float-up 15s infinite ease-in;
    z-index: 1;
}
@keyframes float-up {
    0% {
        transform: translateY(100vh) translateX(0px) rotate(0deg);
        opacity: 0.6;
    }
    50% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-100vh) translateX(100px) rotate(360deg);
        opacity: 0;
    }
}
.heart:nth-child(1) { left: 10%; animation-delay: 0s; }
.heart:nth-child(2) { left: 30%; animation-delay: 3s; }
.heart:nth-child(3) { left: 50%; animation-delay: 6s; }
.heart:nth-child(4) { left: 70%; animation-delay: 9s; }
.heart:nth-child(5) { left: 90%; animation-delay: 12s; }

/* Heading and subtext */
.landing-heading {color:#b30059; font-size:3rem; font-weight:900; text-align:center; margin-bottom:1rem; margin-top:8rem;}
.landing-subtext {color:#b30059; font-size:2rem; font-weight:700; text-align:center; margin-bottom:4rem;}
.floating-heart {color:#ff5c7a; font-size:2rem; display:inline-block; animation: float 3s infinite ease-in-out; margin:0 5px;}
@keyframes float {0%{transform:translateY(0px);}50%{transform:translateY(-10px);}100%{transform:translateY(0px);}}

/* Buttons */
div.stButton>button {
    border-radius:20px !important;
    padding:1.2rem 2.5rem !important;
    font-size:1.5rem !important;
    font-weight:700;
    background-color:#ff8da4 !important;
    color:#fff !important;
    margin:0 10px !important;
    transition: transform 0.3s, background-color 0.3s;
}
div.stButton>button:hover {background-color:#ff5c7a !important; transform:scale(1.1); animation:pulse 1s infinite; cursor:pointer;}
@keyframes pulse {0%{transform:scale(1.1);}50%{transform:scale(1.15);}100%{transform:scale(1.1);}}

/* Message fade-in */
.fade-part {opacity:0; animation: fadeIn 1.5s forwards;}
.fade-part:nth-child(1){animation-delay:0.5s;}
.fade-part:nth-child(2){animation-delay:1.5s;}
.fade-part:nth-child(3){animation-delay:2.5s;}
.fade-part:nth-child(4){animation-delay:3.5s;}
.fade-part:nth-child(5){animation-delay:4.5s;}
.fade-part:nth-child(6){animation-delay:5.5s;}
.fade-part:nth-child(7){animation-delay:6.5s;}
.fade-part:nth-child(8){animation-delay:7.5s;}
.fade-part:nth-child(9){animation-delay:8.5s;}
.fade-part:nth-child(10){animation-delay:9.5s;}
@keyframes fadeIn {0%{opacity:0;}100%{opacity:1;}}
</style>
""", unsafe_allow_html=True)

# Add floating hearts to all pages
st.markdown("""
<div class="heart">❤️</div>
<div class="heart">💖</div>
<div class="heart">💕</div>
<div class="heart">💗</div>
<div class="heart">💓</div>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state: st.session_state.page = "home"
if "photo_index" not in st.session_state: st.session_state.photo_index = 0

def go_to(page):
    st.session_state.page = page

# --- HOME ---
if st.session_state.page == "home":
    st.markdown(
        '<div class="landing-heading">Hey you <span class="floating-heart">&#10084;</span><span class="floating-heart">&#128150;</span></div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="landing-subtext">Open this... if you dare</div>', unsafe_allow_html=True)

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

# --- MESSAGE ---
elif st.session_state.page == "message":

    st.markdown("""
<div style="
    max-width: 700px;
    margin: 80px auto 40px auto;
    padding: 35px;
    border-radius: 20px;
    background-color: white;
    text-align: justify;
    font-size: 1.05rem;
    line-height: 1.8;
    color: #ff4da6;
">
<strong>My love,</strong><br><br>

From the very beginning, you have brought so much light into my life.
Every moment with you feels special, whether we're laughing over something silly
or just sitting quietly together.<br><br>

You make ordinary days feel extraordinary. I am endlessly grateful for
your kindness, your warmth, and the way you care so deeply.<br><br>

Thank you for being you. &#10084;
</div>
""", unsafe_allow_html=True)

    if st.button("🏠 Back"):
        go_to("home")


# --- PHOTOS ---
elif st.session_state.page=="photos":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:2.5rem; font-weight:900; margin-bottom:3rem; margin-top:3rem;">📸 Our Moments ❤️</div>',
        unsafe_allow_html=True
    )

    photos = [
        ("photo1.jpeg","First cute moment"),
        ("photo2.jpeg","Our silly faces"),
        ("photo3.jpeg","Memories together"),
        ("photo4.jpeg","Funny times ❤️")
    ]
    current_photo, caption = photos[st.session_state.photo_index]

    # Centered image with fixed width
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(current_photo, width=500)
        st.markdown(f'<p style="color:#b30059; font-weight:bold; text-align:center; font-size:1.2rem; margin-top:1rem;">{caption}</p>', unsafe_allow_html=True)
        
        # Navigation buttons aligned with photo
        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns(2, gap="small")
        with btn_col1:
            if st.button("⬅️ Previous", key="prev_arrow", use_container_width=True):
                st.session_state.photo_index = (st.session_state.photo_index - 1) % len(photos)
        with btn_col2:
            if st.button("Next ➡️", key="next_arrow", use_container_width=True):
                st.session_state.photo_index = (st.session_state.photo_index + 1) % len(photos)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🏠 Back"):
        go_to("home")


# --- SONG ---
elif st.session_state.page=="song":
    st.markdown('<div style="text-align:center; color:#b30059; font-size:1.7rem; margin-top:5rem;">🎵 My Song for You... reminds me of you ❤️</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🏠 Back"): go_to("home")

# --- EXTRA ---
elif st.session_state.page=="extra":
    st.markdown('<div style="text-align:center; color:#b30059; font-size:2.5rem; font-weight:900; margin-top:5rem; margin-bottom:3rem;">✨ Something Extra... Don\'t Press This 😏</div>', unsafe_allow_html=True)
    
    # Add some mystery text - centered
    st.markdown('<div style="text-align:center; color:#ff5c7a; font-size:1.3rem; margin-bottom:3rem; font-weight:600;">I warned you... but you never listen 😄</div>', unsafe_allow_html=True)
    
    # Initialize session state for showing extra content
    if "show_extra" not in st.session_state:
        st.session_state.show_extra = False
    
    # Center the button - only show if image hasn't been revealed
    if not st.session_state.show_extra:
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("🚫 Do Not Press 🚫", key="danger_button", use_container_width=True):
                st.session_state.show_extra = True
                st.rerun()
    
    # Show image centered if button was pressed
    if st.session_state.show_extra:
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image("funny.jpeg", use_container_width=True)
            st.markdown('<div style="text-align:center; color:#b30059; font-size:1.4rem; font-weight:700; margin-top:1.5rem;">😂 I told you not to press it! 😂</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.show_extra = False
            go_to("home")
            st.rerun()
