import re
import random
import streamlit as st

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    return "".join(random.sample(characters, 12))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", layout="wide")

# Custom CSS for sidebar and animations
st.markdown(
    """
    <style>
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #1F1F1F; /* Dark background */
        color: #FF5722; /* Vibrant orange text */
        padding: 20px;
        border-radius: 10px;
        animation: fadeIn 2s;
    }

    /* Footer text styling */
    .sidebar .sidebar-content p {
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        color: #FF4081; /* Vibrant pink for footer */
        margin-top: 20px;
    }

    /* Fade-in animation */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* Password input field styling */
    input {
        border: 2px solid #FF5722; /* Vibrant border */
        border-radius: 5px;
        padding: 10px;
    }

    /* Suggestions list */
    .suggestions {
        color: #03DAC6; /* Vibrant teal for suggestions */
        margin-left: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Password Strength Meter")
option = st.sidebar.radio("Navigate", ["Check Password Strength", "Generate Strong Password"])

# Add footer text in the sidebar
st.sidebar.markdown("<p>Made with ❤ by Malik</p>", unsafe_allow_html=True)

if option == "Check Password Strength":
    st.title("🔑 Password Strength Checker")
    st.write("Check how strong your password is and get suggestions to improve it!")

    # Input
    password = st.text_input("Enter your password:", type="password")

    if password:
        score, feedback = check_password_strength(password)

        # Display results
        st.subheader("Password Strength:")
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
            st.write("Suggestions:")
            for item in feedback:
                st.write(f"<div class='suggestions'>- {item}</div>", unsafe_allow_html=True)
        else:
            st.error("❌ Weak Password - Improve using the suggestions below:")
            st.write("Suggestions:")
            for item in feedback:
                st.write(f"<div class='suggestions'>- {item}</div>", unsafe_allow_html=True)

elif option == "Generate Strong Password":
    st.title("🔒 Strong Password Generator")
    st.write("Click the button below to generate a secure and strong password.")

    if st.button("Generate Password"):
        strong_password = generate_strong_password()
        st.success(f"Your Strong Password: `{strong_password}`")
