"""
Author: Vema Dondeti
Date: 2025-05-30
Version: 1.0

📚 Interactive Math Tutor Chatbot (Streamlit App)

This Streamlit app serves as an AI-powered math tutor for elementary-level students,
leveraging a fine-tuned GPT-3.5 model to provide age-appropriate explanations for basic math problems.

### Code Overview:
- Imports necessary libraries and sets up OpenAI API access.
- Configures the Streamlit app layout, page settings, and UI behavior.
- Applies custom CSS for styling input fields, buttons, and headers.
- Uses Streamlit's session state to manage app context and user interactions.
- Defines three main tabs:
    1. **Math Tutor** – the core chatbot interface for asking math questions.
    2. **About** – explains the model, scope, and intent of the app.
    3. **Feedback** – collects user ratings and comments (not stored, just printed).
- Allows selection of example questions or entry of custom math questions.
- Generates answers using the fine-tuned model; optionally compares with base GPT-3.5.
- Feedback section demonstrates a collection mechanism (prints to console for now).
- Sidebar gives users quick instructions and project context.

💡 Created as a final project to demonstrate how generative AI can support early education.
"""
import streamlit as st
import os
from openai import OpenAI

# ----------------- Streamlit App Configuration -----------------
# Sets up the main settings for the Streamlit web app.
# - Title and icon reflect the educational theme.
# - "wide" layout allows more space for chatbot and side panel to coexist comfortably.
# - Sidebar is expanded by default to highlight instructions and example prompts.
# - Menu items link to Streamlit community/help and a brief app description.

# This setup ensures the app is user-friendly, visually accessible, and well-structured
# for elementary users and evaluators.

st.set_page_config(
    page_title="Math Tutor Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': "Learn more about this Math Tutor application."
    }
)

# ----------------- Initialize OpenAI Client -----------------
# Sets up the OpenAI client using the API key from environment variables.
# This allows the app to send user prompts and receive AI-generated responses.
# We're using a **fine-tuned GPT-3.5 Turbo model** trained specifically for
# providing age-appropriate, supportive responses to elementary-level math questions.

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
fine_tuned_model = "ft:gpt-3.5-turbo-0125:personal:math-tutor:BVPvM7jo"

# ----------------- Custom CSS Styling -----------------
# Applies custom CSS to enhance the visual appearance of the Streamlit app.
# Styles the header, subheader, input fields, and buttons to make the UI more engaging
# and age-appropriate for elementary students. This improves usability and gives
# the app a friendly, educational look and feel.
# Note: `unsafe_allow_html=True` is used to allow embedding raw HTML/CSS.

st.markdown(
    """
    <style>
    .st-header {
        background-color: #f0f8ff;
        padding: 20px;
        border-bottom: 1px solid #ccc;
    }
    .st-subheader {
        color: #336699;
    }
    .st-text-input > div > div > input {
        border: 2px solid #ADD8E6;
        border-radius: 5px;
        padding: 10px;
    }
    .st-button > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .st-button > button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------- Initialize session state -----------------
# Sets up default values in Streamlit's session state to manage user interactions
# and preserve data across reruns of the app:
# - `fine_tuned_response`: stores the response from the fine-tuned model.
# - `base_model_response`: stores the response from the base GPT-3.5 model (if comparison is enabled).
# - `compare_checked`: tracks whether the user enabled response comparison.
# - `last_input`: keeps the last question asked by the user to avoid redundant API calls.
# - `active_tab`: tracks the currently active tab to retain UI context between interactions.

if "fine_tuned_response" not in st.session_state:
    st.session_state["fine_tuned_response"] = None
if "base_model_response" not in st.session_state:
    st.session_state["base_model_response"] = None
if "compare_checked" not in st.session_state:
    st.session_state["compare_checked"] = False
if "last_input" not in st.session_state:
    st.session_state["last_input"] = ""
if "active_tab" not in st.session_state:
    st.session_state["active_tab"] = "Math Tutor"

# ----------------- Helper functions -----------------
# clear_responses(): Resets all session state variables related to responses and comparison flags.
# This ensures that when the user inputs a new question or selects a different example,
# previous answers are cleared and new API calls can be made for fresh results.

# get_base_model_response(): Fetches a response from the base GPT-3.5-turbo model to compare
# with the fine-tuned model’s answer. This is only done if there is user input and a fine-tuned
# response already available, providing a side-by-side comparison of answers for the same question.


def clear_responses():
    st.session_state["fine_tuned_response"] = None
    st.session_state["base_model_response"] = None
    st.session_state["compare_checked"] = False
    st.session_state["last_input"] = ""


def get_base_model_response():
    # Only fetch base model response if fine-tuned response exists and input present
    question_text = st.session_state.get("current_question", "")
    if question_text and st.session_state["fine_tuned_response"]:
        with st.spinner("Comparing with base model..."):
            st.session_state["base_model_response"] = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question_text}],
                max_tokens=150,
                temperature=0.7,
            )

# ----------------- Tab Setup and UI Logic -----------------
# Define three main tabs: "Math Tutor", "About", and "Feedback".
# Each tab presents a distinct interface and functionality within the app.

# Notes on Tab State
# - Streamlit's current tabs widget does not support programmatic switching.
# - We track the active tab in session_state for informational or logging purposes only.
# - Users manually switch tabs by clicking on the tab headers.


tab_names = ["Math Tutor", "About", "Feedback"]
tab1, tab2, tab3 = st.tabs(tab_names)

# ----------------- Tab 1: Math Tutor -----------------
# - Provides the core chatbot interface for students to ask elementary math questions.
# - Offers a dropdown of example questions or allows users to type their own.
# - When a question is entered or selected, calls the fine-tuned GPT-3.5 model for a tailored response.
# - Displays the AI’s answer with a clear header.
# - Provides an optional checkbox to compare the fine-tuned model's answer with the base GPT-3.5-turbo model's answer.
# - If comparison is requested, fetches and displays the base model’s response side-by-side.
# - Handles API errors gracefully and updates session state to track current inputs and responses.
with tab1:
    st.session_state["active_tab"] = "Math Tutor"
    st.header("📚 Math Tutor Chatbot")
    st.subheader("Ask elementary math questions!")

    example_questions = [
        "Select your own question",
        "What is 5 + 2?",
        "Solve for x: x + 3 = 7",
        "What is half of 10?",
        "How many sides does a triangle have?"
    ]

    selected_question = st.selectbox("Select an example (optional)",
                                     example_questions,
                                     key="selected_question",
                                     on_change=clear_responses)

    # Determine user question from selectbox or text input
    if selected_question == "Select your own question":
        user_input = st.text_input("Your question:", key="user_question")
    else:
        user_input = selected_question

    st.session_state["current_question"] = user_input  # save current question to session

    if user_input:
        # Only fetch fine-tuned response if input changed
        if st.session_state["fine_tuned_response"] is None or st.session_state["last_input"] != user_input:
            with st.spinner("Thinking..."):
                try:
                    st.session_state["fine_tuned_response"] = client.chat.completions.create(
                        model=fine_tuned_model,
                        messages=[{"role": "user", "content": user_input}],
                        max_tokens=150,
                        temperature=0.7
                    )
                    st.session_state["base_model_response"] = None
                    st.session_state["last_input"] = user_input
                    st.session_state["compare_checked"] = False
                except Exception as e:
                    st.error(f"An error occurred: {e}")

        # Show fine-tuned answer
        if st.session_state["fine_tuned_response"]:
            st.markdown("### Answer:")
            st.info(f"🤖 {st.session_state['fine_tuned_response'].choices[0].message.content}")

            # Checkbox to compare with base model, triggers fetch when checked
            compare_base = st.checkbox(
                "Compare with base model (gpt-3.5-turbo)",
                key="compare_checkbox",
                value=st.session_state["compare_checked"],
            )
            if compare_base and not st.session_state["base_model_response"]:
                get_base_model_response()
            st.session_state["compare_checked"] = compare_base

            # Show both answers if compare checked and base response present
            if compare_base and st.session_state["base_model_response"]:
                st.markdown("### Comparison with Base Model:")
                st.info(f"🤖 (Fine-Tuned): {st.session_state['fine_tuned_response'].choices[0].message.content}")
                st.info(f"🤖 (Base): {st.session_state['base_model_response'].choices[0].message.content}")
            elif not compare_base:
                st.session_state["base_model_response"] = None

# ----------------- Tab 2: About -----------------
# - Explains the purpose of the app and details about the fine-tuned model.
# - Shares insights on the training dataset topics (basic arithmetic, fractions, simple geometry).
# - Offers usage tips for best results.
# - Provides transparency on the model versions used.
# - Serves to build trust and understanding for users and stakeholders.

with tab2:
    st.session_state["active_tab"] = "About"
    st.header("About This Math Tutor Application")
    st.markdown("""
    This application is designed to be a friendly and helpful math tutor for elementary school students.
    It uses a **fine-tuned GPT-3.5-turbo model** to answer math questions in a clear and age-appropriate way.

    ### 🔍 How It Works:
    The AI was fine-tuned on a dataset of math problems covering:
    - Basic arithmetic (addition, subtraction, multiplication, division)
    - Introduction to fractions
    - Simple geometry (shapes, sides)
    - Word problems

    The model is designed to be supportive and explain concepts clearly, often with encouraging language.

    ### 💡 Usage Tips:
    - Ask clear and simple math questions
    - Best used for elementary-level math
    - Try rephrasing if a response seems unclear

    ### 🤖 Model Details:
    - **Base Model:** gpt-3.5-turbo-0125
    - **Fine-tuned Model :** Custom fine-tuned version for elementary-level math tutoring

    """)

# ----------------- Tab 3: Feedback -----------------
# - Provides a simple interface for users to submit comments and rate the tutor’s helpfulness.
# - Collects feedback via a text area and a radio button rating.
# - On submission, thanks the user and prints the feedback to the console.
# - Feedback is not persisted in this version, but the UI demonstrates how to gather it for future extension.
with tab3:
    st.session_state["active_tab"] = "Feedback"
    st.header("Feedback")
    st.markdown("We'd love to hear your thoughts on how to make this Math Tutor better!")

    feedback_text = st.text_area("Your comments or suggestions:", key="feedback_text_area")

    # Important: Do NOT change tabs automatically when radio is changed
    rating = st.radio(
        "How helpful was the tutor?",
        ["Not Helpful", "Slightly Helpful", "Helpful", "Very Helpful"],
        index=None,
        key="feedback_rating_radio",
        on_change=None  # no tab switch triggered here
    )

    submit_button = st.button("Submit Feedback", key="feedback_submit_button")

    if submit_button:
        feedback_data = {
            "comment": feedback_text,
            "rating": rating,
        }
        st.success("Thank you for your feedback!")
        print("Feedback submitted:", feedback_data)

# ----------------- Sidebar Content -----------------
# - Presents quick informational snippets about the app and instructions.
# - Reinforces app purpose and navigation tips for first-time users.

with st.sidebar:
    st.header("Quick Info")
    st.markdown("📚 **Elementary Math Tutor**")
    st.markdown("Ask questions in the *Math Tutor* tab.")
    st.markdown("Learn more about this application in the About tab.")
