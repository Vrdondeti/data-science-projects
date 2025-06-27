# Interactive AI Math Tutor Chatbot

An educational chatbot that helps elementary school students learn math through clear, step-by-step explanations. Built with Streamlit and a fine-tuned version of OpenAI’s GPT-3.5-turbo.

---

## Project Overview

This project fine-tunes GPT-3.5-turbo to provide age-appropriate, encouraging, and understandable math explanations. It especially supports learners whose questions may be vaguely phrased.

---

## Motivation

- Base LLMs solve math but often offer formal, textbook-style responses.
- Children benefit more from warm tones, positive reinforcement, and engaging analogies.
- Aim: Improve clarity, tone, and engagement for young users.

---

## Features

- **Interactive Q&A**: Type any elementary-level math question.
- **Example Prompts**: Pre-set sample questions to guide user interaction.
- **Model Comparison**: View responses from both the fine-tuned model and base GPT-3.5-turbo.
- **Feedback Form**: Submit comments and ratings about explanations.

---

## Tech Stack & Models

- **Backend**: OpenAI GPT-3.5-turbo (base) and fine-tuned model  
- **Frontend**: Streamlit for interface and logging user feedback
- **Fine-Tuning Data**: Custom JSONL dataset with friendly, emoji-enhanced explanations

---

## Fine-Tuning Process

1. **Dataset Creation**  
   - Built a JSONL file of user–assistant pairs following OpenAI schema  
   - Ensured engaging, age-appropriate responses

2. **Model Training**  
   - Uploaded dataset using `openai` CLI 
   - Monitored via API endpoints

3. **Metrics Logged**  
   - Training Loss: ~0.529  
   - Training Accuracy: ~0.848

4. **Evaluation**  
   - Compared base and fine-tuned responses  
   - Adjusted `max_tokens` to avoid truncation  
   - Fine-tuned responses showed improved tone and clarity

---

## Installation & Usage

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/math-tutor-chatbot.git
   cd math-tutor-chatbot

2. Install requirements
   pip install -r requirements.txt

3. Set your OpenAI API key
   This app uses OpenAI's API to generate responses from a fine-tuned GPT-3.5 model. To run the app, you need an OpenAI API key.

   - How to get your OpenAI API key:

      1. Sign up or log in at [OpenAI](https://platform.openai.com/).
      2. Navigate to your account's API keys section.
      3. Create a new secret key or use an existing one.

   - How to set the API key for this app:

      - Locally, create a `.env` file in your project folder with the following line:
          OPENAI_API_KEY=your_api_key_here

      - Or export it in your terminal session:
          ```bash
          export OPENAI_API_KEY=your_api_key_here

4. Launch the Streamlit app
   streamlit run app.py