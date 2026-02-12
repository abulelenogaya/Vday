import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="wide")

# --- CSS ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f0 0%, #ffc0cb 100%);
    font-family: 'Comic Sans MS', cursive, sans-serif;
}

/* Board wrapper */
.board-container {
    border: 5px solid #ff8da4;
    border-radius: 25px;
    padding: 3rem 2rem;
    max-width: 700px;
    margin: 80px auto; /* horizontal center + vertical spacing */
    background: linear-gradient(135deg, #fff0f5 0%, #ffe6f0 100%);
    text-align: center;
    box-shadow: 0 8px 20px rgba(255,140,164,0.3);
}

/* Heading */
.board-heading {
    font-size: 2.8rem;
    font-weight: 900;
    color: #b30059;
    margin-bottom: 1.5rem;
}

/* Subtext */
.board-text {
    font-size: 2rem;
    font-weight: 700;
    color: #b30059;
    margin-bottom: 2.5rem;
}

/* Buttons */
div.stButton > button {
    border-radius: 20px !important;
    padding: 1.2rem 2.5rem !important;
    font-size: 1.4rem !important;
    font-weight: 700;
    background-color: #ff8da4 !important;
    color: #fff !important;
    margin: 0 10px !important;
    transition: transform 0.2s, background-color 0.2s;
}
div.stButton > button:hover {
    background-color: #ff5c7a !important;
    transform: scale(1.05);
    cursor: pointer;
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
    with st.container():
        st.markdown("<div class='board-container'>", unsafe_allow_html=True)
        st.markdown("<div class='board-heading'>Hey you ❤️</div>", unsafe_allow_html=True)
        st.markdown("<div class='board-text'>Open this… if you dare 😏</div>", unsafe_allow_html=True)

        # Buttons inside the board
        cols = st.columns(4)
        if cols[0].button("💌 A Message"):
            go_to("message")
        if cols[1].button("🎵 My Song for You"):
            go_to("song")
        if cols[2].button("📸 Our Moments"):
            go_to("photos")
        if cols[3].button("✨ Something Extra"):
            go_to("extra")

        st.markdown("</div>", unsafe_allow_html=True)

# --- Other pages remain same ---
elif st.session_state.page == "message":
    st.markdown("<div class='board-text'>So… I was going to play it cool. But that’s clearly not happening 😏 I like you… ❤️</div>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")
elif st.session_state.page == "photos":
    st.markdown("<div class='board-text'>📸 Our Moments ❤️</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.image("photo1.jpeg")
    col1.image("photo3.jpeg")
    col2.image("photo2.jpeg")
    col2.image("photo4.jpeg")
    if st.button("Back"):
        go_to("home")
elif st.session_state.page == "song":
    st.markdown("<div class='board-text'>🎵 My Song for You… reminds me of you ❤️</div>", unsafe_allow_html=True)
    if st.button("Back"):
        go_to("home")
elif st.session_state.page == "extra":
    st.markdown("<div class='board-text'>✨ Don’t Press This… 😏</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    if col1.button("Do Not Press 😏"):
        col1.image("funny.jpeg")
    if st.button("Back"):
        go_to("home")
