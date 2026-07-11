import streamlit as st

st.set_page_config(
    page_title="Sowmya Kids World ⭐",
    page_icon="🌈",
    layout="wide"
)

# --------------------
# CSS
# --------------------

st.markdown("""
<style>

.main{
background:linear-gradient(135deg,#FFD54F,#4FC3F7);
}

h1{
text-align:center;
color:#E91E63;
}

.quiz{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 5px 12px gray;
}

</style>
""", unsafe_allow_html=True)

st.title("🌈 Sowmya Kids World ⭐")

st.write("### Learn • Play • Smile 😊")

score = 0

tab1, tab2, tab3, tab4 = st.tabs(
    ["🔤 Alphabet", "🔢 Numbers", "🎨 Colors", "🧠 Quiz"]
)

with tab1:
    st.header("Alphabet")
    st.write("A 🍎 Apple")
    st.write("B ⚽ Ball")
    st.write("C 🐱 Cat")
    st.write("D 🐶 Dog")

with tab2:
    st.header("Numbers")
    st.write("1️⃣ One")
    st.write("2️⃣ Two")
    st.write("3️⃣ Three")
    st.write("4️⃣ Four")
    st.write("5️⃣ Five")

with tab3:
    st.header("Colors")
    st.success("🟢 Green")
    st.info("🔵 Blue")
    st.warning("🟡 Yellow")
    st.error("🔴 Red")

with tab4:

    st.header("Fun Quiz")

    q1 = st.radio(
        "Which animal barks?",
        ["Cat", "Dog", "Lion"]
    )

    if q1 == "Dog":
        score += 1

    q2 = st.radio(
        "Which comes after 2?",
        ["3", "5", "7"]
    )

    if q2 == "3":
        score += 1

    q3 = st.radio(
        "What color is a banana?",
        ["Yellow", "Blue", "Pink"]
    )

    if q3 == "Yellow":
        score += 1

    if st.button("Check Score"):

        st.success(f"⭐ Your Score: {score}/3")

        if score == 3:
            st.balloons()
            st.success("🎉 Excellent! You're a Super Learner!")