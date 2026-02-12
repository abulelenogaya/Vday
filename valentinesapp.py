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
    color: #333333;  /* dark text for readability */
}

/* Card styling */
.card {
    background-color: #ffffffcc;  /* slightly transparent white */
    padding: 2.5rem;
    border-radius: 20px;
    box-shadow: 0px 6px 25px rgba(255, 182, 193, 0.3); /* soft pink shadow */
    margin-bottom: 2rem;
}

/* Center alignment */
.center { text-align: center; }

/* Streamlit button overrides */
div.stButton > button {
    border-radius: 15px !important;
    padding: 1rem 2rem !important;
    font-size: 1.2rem !important;
    font-weight: 600;
    background-color: #ff8da4 !important;  /* bright pink */
    color: #fff !important;  /* white text */
    width: 180px;  /* uniform width */
    margin: 0 10px;  /* horizontal spacing */
    transition: transform 0.2s, background-color 0.2s;
}
div.stButton > button:hover {
    background-color: #ff5c7a !important;  /* darker pink on hover */
    transform: scale(1.05);
    cursor: pointer;
}

/* Decorative hearts */
.hearts {
    text-align: center;
    font-size: 1.5rem;
    margin-bottom: 1rem;
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
    st.markdown("<div class='card center'>", unsafe_allow_html=True)
    st.markdown("<div class='hearts'>💖 💕 💗 💖 💕 💗 💖</div>", unsafe_allow_html=True)
    st.markdown("## Hey you ❤️")
    st.markdown("Open this… if you dare 😏")
    st.markdown("<br>", unsafe_allow_html=True)

    # Horizontal buttons using columns
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("💌 A Message"):
            go_to("message")
    with col2:
        if st.button("🎵 My Song for You"):
            go_to("song")
    with col3:
        if st.button("📸 Our Moments"):
            go_to("photos")

    # Extra button below
    if st.button("✨ Something Extra"):
        go_to("extra")

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

I like our little moments. The way our conversations shift from playful to… something else.  
The tension. The ease. The way it feels exciting but natural.  

Just know… I’m very aware of the effect you have on me.  

And I don’t hate it. ❤️
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
        st.image("photo1.jpeg", caption="This smile? Dangerous 😏")
        st.image("photo2.jpeg", caption="We look a little too good here ❤️")
    with col2:
        st.image("photo3.jpeg", caption="I replay this day sometimes 🫶")
        st.image("photo4.jpeg", caption="You. Just… you 😘")

    if st.button("Back"):
        go_to("menu")

# --- SONG PAGE ---
elif st.session_state.page == "song":
    st.markdown("## 🎵 My Song for You")
    st.markdown("This one reminds me of you… ❤️")
    st.markdown("""
It talks about someone who makes the singer smile and feel loved… kind of like how you make me feel 😏  

Soft, a little intense… just like the effect you have on me.
""")
    if st.button("Back"):
        go_to("menu")

# --- EXTRA PAGE ---
elif st.session_state.page == "extra":
    st.markdown("## ✨ Don’t Press This…")
    if st.button("Do Not Press 😏"):
        st.image("funny.jpeg", caption="Couldn’t resist… this is too good 😏 You make me smile every time ❤️")
    if st.button("Back"):
        go_to("menu")
