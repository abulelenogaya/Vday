import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
/* Soft pink ombre background */
.stApp {
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 100%);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Pink board enclosing landing content */
.landing-board {
    border: 5px solid #ff8da4;
    border-radius: 25px;
    padding: 4rem 3rem;
    max-width: 900px;
    width: 90%;
    background: linear-gradient(135deg, #fff0f5 0%, #ffe6f0 100%);
    text-align: center;
    box-shadow: 0 8px 20px rgba(255,140,164,0.3);
}

/* Heading */
.landing-heading {
    color: #b30059;
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 1.5rem;
    text-align: center;
}

/* Subtext */
.landing-text {
    color: #b30059;
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 3rem;
    text-align: center;
}

/* General page text */
.page-text {
    font-size: 1.5rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    color: #b30059;
    text-align: center;
}

/* Streamlit buttons */
div.stButton > button {
    border-radius: 20px !important;
    padding: 1.2rem 2.5rem !important;
    font-size: 1.5rem !important;
    font-weight: 700;
    background-color: #ff8da4 !important;
    color: #fff !important;
    margin: 0 15px !important;
    transition: transform 0.2s, background-color 0.2s;
}
div.stButton > button:hover {
    background-color: #ff5c7a !important;
    transform: scale(1.05);
    cursor: pointer;
}

/* Images */
img {
    max-width: 100%;
    border-radius: 15px;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Navigation Function ---
def go_to(page_name):
    st.session_state.page = page_name

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.markdown("<div class='landing-board'>", unsafe_allow_html=True)
    st.markdown("<div class='landing-heading'>Hey you ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='landing-text'>Open this… if you dare 😏</div>", unsafe_allow_html=True)

    # Horizontal buttons (all 4 centered)
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        if st.button("💌 A Message"):
            go_to("message")
    with col2:
        if st.button("🎵 My Song for You"):
            go_to("song")
    with col3:
        if st.button("📸 Our Moments"):
            go_to("photos")
    with col4:
        if st.button("✨ Something Extra"):
            go_to("extra")

    st.markdown("</div>", unsafe_allow_html=True)

# --- MESSAGE PAGE ---
elif st.session_state.page == "message":
    st.markdown("<div class='page-text'>", unsafe_allow_html=True)
    st.markdown("""
So… I was going to play it cool.  

But that’s clearly not happening 😏  

I like you. And not in a subtle way.  
In a “catching myself smiling at my phone” kind of way.  

I like our little moments. The way our conversations shift from playful to… something else.  
The tension. The ease. The way it feels exciting but natural.  

Just know… I’m very aware of the effect you have on me.  

And I don’t hate it. ❤️
""", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")
    st.markdown("</div>", unsafe_allow_html=True)

# --- PHOTOS PAGE ---
elif st.session_state.page == "photos":
    st.markdown("<div class='page-text'>📸 Our Moments<br>Little memories, just for us ❤️</div>", unsafe_allow_html=True)

    # Split images for spacing
    col1, col2 = st.columns(2)
    with col1:
        st.image("photo1.jpeg", caption="This smile? Dangerous 😏")
        st.image("photo3.jpeg", caption="I replay this day sometimes 🫶")
    with col2:
        st.image("photo2.jpeg", caption="We look a little too good here ❤️")
        st.image("photo4.jpeg", caption="You. Just… you 😘")

    if st.button("Back"):
        go_to("home")

# --- SONG PAGE ---
elif st.session_state.page == "song":
    st.markdown("<div class='page-text'>🎵 My Song for You<br>This one reminds me of you… ❤️<br>It talks about someone who makes the singer smile and feel loved… kind of like how you make me feel 😏<br>Soft, a little intense… just like the effect you have on me.</div>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown("<div class='page-text'>✨ Don’t Press This…<br>You’ve been warned 😏</div>", unsafe_allow_html=True)

    # Horizontal layout for extra content
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Do Not Press 😏"):
            st.image("funny.jpeg", caption="Couldn’t resist… this is too good 😏 You make me smile every time ❤️")
    with col2:
        st.markdown("<div class='page-text'>Just for fun… nothing too serious 😉</div>", unsafe_allow_html=True)

    if st.button("Back"):
        go_to("home")
