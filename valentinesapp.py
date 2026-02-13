import streamlit as st

st.set_page_config(page_title="For You", page_icon="💌", layout="wide")

# --- CSS ---
st.markdown("""
<style>
/* Remove top padding */
.css-18e3th9 {padding-top:0rem; padding-bottom:0rem;}

/* Main app background */
.stApp {
    font-family: 'Comic Sans MS', cursive, sans-serif; 
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 30%, #ffb6c1 60%, #ff8da4 100%);
}

/* Floating hearts animation - using absolute positioning within viewport */
.hearts-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}
.heart {
    position: absolute;
    font-size: 3rem;
    opacity: 0.4;
    animation: float-up 15s infinite ease-in;
}
@keyframes float-up {
    0% {
        transform: translateY(100vh) translateX(0px) rotate(0deg);
        opacity: 0.4;
    }
    50% {
        opacity: 0.5;
    }
    100% {
        transform: translateY(-20vh) translateX(80px) rotate(360deg);
        opacity: 0;
    }
}
.heart:nth-child(1) { left: 5%; animation-delay: 0s; }
.heart:nth-child(2) { left: 15%; animation-delay: 2s; }
.heart:nth-child(3) { left: 25%; animation-delay: 4s; }
.heart:nth-child(4) { left: 35%; animation-delay: 6s; }
.heart:nth-child(5) { left: 45%; animation-delay: 8s; }
.heart:nth-child(6) { left: 55%; animation-delay: 10s; }
.heart:nth-child(7) { left: 65%; animation-delay: 12s; }
.heart:nth-child(8) { left: 75%; animation-delay: 1s; }
.heart:nth-child(9) { left: 85%; animation-delay: 3s; }
.heart:nth-child(10) { left: 95%; animation-delay: 5s; }
.heart:nth-child(11) { left: 10%; animation-delay: 7s; }
.heart:nth-child(12) { left: 20%; animation-delay: 9s; }
.heart:nth-child(13) { left: 30%; animation-delay: 11s; }
.heart:nth-child(14) { left: 40%; animation-delay: 13s; }
.heart:nth-child(15) { left: 50%; animation-delay: 0.5s; }
.heart:nth-child(16) { left: 60%; animation-delay: 2.5s; }
.heart:nth-child(17) { left: 70%; animation-delay: 4.5s; }
.heart:nth-child(18) { left: 80%; animation-delay: 6.5s; }
.heart:nth-child(19) { left: 90%; animation-delay: 8.5s; }
.heart:nth-child(20) { left: 8%; animation-delay: 10.5s; }
.heart:nth-child(21) { left: 18%; animation-delay: 12.5s; }
.heart:nth-child(22) { left: 28%; animation-delay: 1.5s; }
.heart:nth-child(23) { left: 38%; animation-delay: 3.5s; }
.heart:nth-child(24) { left: 48%; animation-delay: 5.5s; }
.heart:nth-child(25) { left: 58%; animation-delay: 7.5s; }
.heart:nth-child(26) { left: 68%; animation-delay: 9.5s; }
.heart:nth-child(27) { left: 78%; animation-delay: 11.5s; }
.heart:nth-child(28) { left: 88%; animation-delay: 13.5s; }
.heart:nth-child(29) { left: 12%; animation-delay: 14s; }
.heart:nth-child(30) { left: 92%; animation-delay: 14.5s; }

/* Heading and subtext */
.landing-heading {color:#b30059; font-size:3rem; font-weight:900; text-align:center; margin-bottom:1rem; margin-top:8rem; position:relative; z-index:10;}
.landing-subtext {color:#b30059; font-size:2rem; font-weight:700; text-align:center; margin-bottom:4rem; position:relative; z-index:10;}
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
    position:relative;
    z-index:10;
}
div.stButton>button:hover {background-color:#ff5c7a !important; transform:scale(1.1); animation:pulse 1s infinite; cursor:pointer;}
@keyframes pulse {0%{transform:scale(1.1);}50%{transform:scale(1.15);}100%{transform:scale(1.1);}}

/* Ensure content is above floating hearts */
.element-container {
    position: relative;
    z-index: 10;
}

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

# Add floating hearts to all pages - more hearts!
st.markdown("""
<div class="hearts-container">
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
    <div class="heart">💗</div>
    <div class="heart">💓</div>
    <div class="heart">💖</div>
    <div class="heart">💕</div>
</div>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state: st.session_state.page = "home"
if "photo_index" not in st.session_state: st.session_state.photo_index = 0

def go_to(page):
    st.session_state.page = page

# --- HOME ---
if st.session_state.page == "home":
    st.markdown(
        '<div class="landing-heading">Happy Valentine\'s Day My Love <span class="floating-heart">&#10084;</span></div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="landing-subtext">I made something for you... I hope you\'ll like it🥺</div>', unsafe_allow_html=True)

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
    padding: 40px;
    border-radius: 20px;
    background-color: white;
    text-align: justify;
    font-size: 1.05rem;
    line-height: 1.6;
    color: #ff4da6;
    box-shadow: 0 8px 32px rgba(255, 105, 180, 0.3);
">
So... I was going to play it cool.<br>
But that's clearly not happening 😏<br>
<br>
I like you. And not in a subtle way.<br>
In a "catching myself smiling at my phone" kind of way.<br>
<br>
You've been on my mind a little more than I'd like to admit. (Don't let it get to your head lol..)<br>
<br>
I like our little moments. The way our conversations shift from playful to... something else.<br>
The tension. The ease. The way it feels exciting but natural.<br>
<br>
Just know... I'm very aware of the effect you have on me.<br>
And I don't hate it. &#10084;<br>
<br>
This is still new, and I think that's my favorite part. We're still discovering each other.<br>
Still learning the details. Still choosing to lean in. And I just want you to know that I've been really enjoying it.<br>
Enjoying you.<br>
<br>
I don't know exactly where this goes yet. But I know that right now, I'm grateful it's you I'm getting to explore this with.<br>
And that feels special to me.<br>
<br>
&#10084;
</div>
""", unsafe_allow_html=True)

    if st.button("🏠 Back"):
        go_to("home")


# --- PHOTOS ---
elif st.session_state.page=="photos":
    st.markdown(
        '<div style="text-align:center; color:#b30059; font-size:2.5rem; font-weight:900; margin-bottom:2rem; margin-top:3rem;">📸 Our Moments ❤️</div>',
        unsafe_allow_html=True
    )

    photos = [
        ("photo1.jpeg","I still can't believe I cried like this after the first link 🤭"),
        ("photo2.jpeg","We look a little too cute here ❤️"),
        ("photo3.jpeg","I always have fun with you🫶"),
        ("photo4.jpeg","My main character😘")
    ]
    current_photo, caption = photos[st.session_state.photo_index]

    # Use container to center everything together
    st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
    
    # Single centered column
    col1, col2, col3 = st.columns([1.5,1,1.5])
    
    with col2:
        st.image(current_photo, use_container_width=True)
        
        # Caption
        st.markdown(f'<p style="color:#b30059; font-weight:bold; text-align:center; font-size:1.2rem; margin-top:0.5rem; margin-bottom:1rem;">{caption}</p>', unsafe_allow_html=True)
        
        # Navigation buttons - centered and close together
        btn_col1, btn_col2 = st.columns([1, 1], gap="small")
        with btn_col1:
            if st.button("⬅️ Prev", key="prev_arrow", use_container_width=True):
                st.session_state.photo_index = (st.session_state.photo_index - 1) % len(photos)
                st.rerun()
        with btn_col2:
            if st.button("Next ➡️", key="next_arrow", use_container_width=True):
                st.session_state.photo_index = (st.session_state.photo_index + 1) % len(photos)
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Back button centered
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🏠 Back", use_container_width=True):
            go_to("home")
            st.rerun()


# --- SONG ---
elif st.session_state.page=="song":
    st.markdown('<div style="text-align:center; color:#b30059; font-size:2.5rem; font-weight:900; margin-top:5rem; margin-bottom:1rem;">🎵 My Song for You</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; color:#ff5c7a; font-size:1.3rem; font-weight:600; margin-bottom:2rem;">This one reminds me of you... ❤️<br>It says - you are my smile. you are my love.</div>', unsafe_allow_html=True)
    
    # Spotify embed centered
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Spotify embed for "Wena" by Internet Athi
        st.components.v1.iframe(
            "https://open.spotify.com/embed/track/69qJqxCXyZhaVjgqZEzrdq?utm_source=generator",
            height=352,
            scrolling=False
        )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Back button centered
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🏠 Back", use_container_width=True): 
            go_to("home")
            st.rerun()

# --- EXTRA ---
elif st.session_state.page=="extra":
    # Reset show_extra when first entering the page
    if "extra_page_loaded" not in st.session_state:
        st.session_state.show_extra = False
        st.session_state.extra_page_loaded = True
    
    st.markdown('<div style="text-align:center; color:#b30059; font-size:2.5rem; font-weight:900; margin-top:5rem; margin-bottom:3rem;">✨ Something Extra... Don\'t Press This 😏</div>', unsafe_allow_html=True)
    
    # Initialize session state for showing extra content
    if "show_extra" not in st.session_state:
        st.session_state.show_extra = False
    
    # Center the button - only show if image hasn't been revealed
    if not st.session_state.show_extra:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("🚫 Do Not Press 🚫", key="danger_button", use_container_width=True):
                st.session_state.show_extra = True
                st.rerun()
    
    # Show warning text and image only after button is pressed
    if st.session_state.show_extra:
        # Warning text appears with the image
        st.markdown('<div style="text-align:center; color:#ff5c7a; font-size:1.3rem; margin-bottom:2rem; font-weight:600;">I warned you... but you never listen 😄</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image("funny.jpeg", use_container_width=True)
            st.markdown('<div style="text-align:center; color:#b30059; font-size:1.4rem; font-weight:700; margin-top:1.5rem;">😂 I told you not to press it! 😂</div>', unsafe_allow_html=True)
    
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.show_extra = False
            if "extra_page_loaded" in st.session_state:
                del st.session_state.extra_page_loaded
            go_to("home")
            st.rerun()
