import streamlit as st

st.set_page_config(page_title="Aariv Prototype")
st.title("Aariv – AI Companion for Youth Mental Wellness")

st.write("A simple prototype demonstrating 3 core features: AI Chat, Mood Check-ins, and Coping Tools.")

#1. MOOD CHECK-IN
st.header("😊 Mood Check-in")
mood = st.radio(
    "How are you feeling today?",
    ["🙂 Happy", "😐 Neutral", "☹️ Sad"]
)
if st.button("Submit Mood"):
    st.success(f"Your mood '{mood}' has been recorded. Thank you for sharing!")

#2. AI CHAT (mock version)
st.header("🗨️ Anonymous AI Chat")
user_input = st.text_input("Type your message here:")
if user_input:
    if "exam" in user_input.lower():
        st.write("🤖 Aariv: I understand exams can be stressful. Let's try a 1-minute breathing exercise together.")
    else:
        st.write("🤖 Aariv: Thanks for sharing. Remember, your feelings are valid and I’m here to support you.")

#3. COPING TOOL
st.header("Instant Coping Tool")
if st.button("Start Breathing Exercise"):
    st.info("🌬️ Inhale... Hold... Exhale... Repeat this for 1 minute. You're doing great!")
