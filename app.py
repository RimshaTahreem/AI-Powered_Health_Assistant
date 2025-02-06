import streamlit as st
from transformers import pipeline

# Initialize the text generation model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    user_input = user_input.lower()

    responses = {
        "symptom": "I recommend consulting a healthcare professional for accurate diagnosis.",
        "appointment": "Would you like to schedule an appointment with a doctor?",
        "medication": "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor.",
        "fever": "A fever is usually a sign of infection. Drink fluids, rest, and consult a doctor if it persists.",
        "headache": "Headaches can be caused by many things, such as stress or dehydration. Try drinking water and resting.",
        "cough": "A cough can be caused by a cold or flu. Stay hydrated, and if it persists, see a doctor.",
        "cold": "Common cold symptoms include a runny nose, sore throat, and mild fever. Rest and drink fluids.",
        "diabetes": "Diabetes is a chronic condition that affects your body's ability to regulate blood sugar. It's important to follow your doctor's advice.",
        "hypertension": "Hypertension is high blood pressure. It's important to monitor your blood pressure and maintain a healthy lifestyle.",
        "heart disease": "Heart disease includes a range of conditions that affect the heart. A balanced diet, exercise, and regular check-ups are essential.",
        "covid": "COVID-19 is a viral infection. Stay safe by wearing masks, washing hands frequently, and maintaining social distance.",
        "stroke": "A stroke is a medical emergency. Symptoms include sudden numbness, confusion, and trouble speaking. Call emergency services immediately.",
        "allergy": "Allergies can cause symptoms like sneezing and itching. If symptoms persist, consult your doctor.",
        "mental health": "Mental health is just as important as physical health. If you're feeling overwhelmed, consider speaking to a mental health professional.",
        "exercise": "Exercise is essential for maintaining a healthy body. Aim for at least 30 minutes of moderate activity most days of the week.",
        "nutrition": "Proper nutrition is key to staying healthy. Ensure a balanced diet with plenty of fruits, vegetables, and whole grains.",
        "weight loss": "Weight loss requires a combination of healthy eating, exercise, and lifestyle changes. Consult a nutritionist for a personalized plan.",
        "stress": "Stress management techniques include deep breathing, meditation, and regular physical activity.",
        "sleep": "Good sleep hygiene includes keeping a consistent bedtime, reducing screen time before bed, and creating a relaxing sleep environment.",
    }

    for keyword, response in responses.items():
        if keyword in user_input:
            return response

    # AI-generated response for other inputs
    response = chatbot(user_input, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']

def main():
    st.title("🩺 Healthcare Assistant Chatbot")

    # Initialize session state to store feedback status and user input
    if "feedback_given" not in st.session_state:
        st.session_state.feedback_given = False
        st.session_state.response = ""
        st.session_state.feedback_message_shown = False  # Flag for feedback thank you message

    # Show text input and submit button initially
    user_input = st.text_input("How can I assist you today?", key="user_input")

    if user_input and not st.session_state.feedback_given:
        if st.button("Submit"):
            with st.spinner("Processing your query... Please wait"):
                response = healthcare_chatbot(user_input)
                st.session_state.response = response

            st.success("**Healthcare Assistant:** " + response)

    # Show feedback section after response is generated
    if st.session_state.response and not st.session_state.feedback_given:
        feedback = st.radio("Was this response helpful?", ("Select an option", "Yes", "No"), key="feedback_radio")

        if st.button("Submit Feedback"):
            if feedback == "Yes":
                st.session_state.feedback_message_shown = True
                st.session_state.feedback_given = True  # Mark feedback as given
                st.success("✅ Thank you for your feedback! 😊")
            elif feedback == "No":
                suggestion = st.text_area("What would you like to improve?", key="suggestion_input")
                if st.button("Submit Suggestion"):
                    st.success("🙌 Thank you for your suggestions! We appreciate your input.")
                    st.session_state.feedback_given = True  # Mark feedback as given

    # Option to reset the conversation (clear session state)
    if st.session_state.feedback_given and st.session_state.feedback_message_shown:
        if st.button("Start New Conversation"):
            # Reset session state and start new conversation
            st.session_state.clear()  # Clear session state for a fresh start
            st.experimental_rerun()  # Rerun the script

if __name__ == "__main__":
    main()
