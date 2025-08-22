import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="AI Email Generator", page_icon="📧", layout="wide")

st.title("📧 Smart AI Email Generator")
st.write("Fill in the details below and generate a professional email instantly.")

# --- Recipient Dropdown with Custom Option ---
recipient_options = ["Manager", "HR Head", "IT Officer", "Other"]
recipient_choice = st.selectbox("Recipient", recipient_options)
recipient = st.text_input("Enter Custom Recipient", "Colleague") if recipient_choice == "Other" else recipient_choice

# --- Subject ---
subject = st.text_input("Email Subject", "Weekly Progress Report")

# --- Date ---
email_date = st.date_input("Date", value=date.today())

# --- Background Context ---
background = st.text_area(
    "Background Context",
    "This week we completed the data analysis phase but faced delays due to API issues. "
    "Our target for next week is to deploy the automation module."
)

# --- Tone / Salutation / Closing / Sender ---
tone = st.selectbox("Tone", ["formal", "semi-formal", "casual"], index=0)
salutation = st.selectbox("Salutation", ["Dear", "Respected", "Hello"])
closing = st.selectbox("Closing", ["Regards", "Best regards", "Yours faithfully", "Sincerely"])
sender = st.text_input("Sender's Name", "Hareem")

# --- Generate Button ---
if st.button("✨ Generate Email"):
    with st.spinner("Crafting your email..."):
        try:
            response = requests.post(
                "http://127.0.0.1:5000/generate-email",
                json={
                    "recipient": recipient,
                    "subject": subject,
                    "date": str(email_date),
                    "background": background,
                    "tone": tone,
                    "salutation": salutation,
                    "closing": closing,
                    "sender": sender
                },
                timeout=60
            )

            if response.status_code == 200:
                email_text = response.json().get("email", "").strip()

                if email_text:
                    st.success("✅ Email generated successfully!")

                    # Simple box with built-in copy button
                    st.code(email_text, language="markdown")
                    st.write("👉 Use the copy icon (top right of the box).")
                else:
                    st.warning("⚠️ The model didn’t return any text. Try again.")
            else:
                st.error(f"Backend error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Connection error: {e}")
