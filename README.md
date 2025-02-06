# AI-Powered_Health_Assistant
# Healthcare Assistant Chatbot

A healthcare assistant chatbot built with **Streamlit**, **Transformers**, **TensorFlow**, and **NLTK**. This chatbot provides users with health-related advice based on their inputs and offers the ability to submit feedback for improving the system.

## Features

- **Text Generation:** Utilizes the pre-trained **DistilGPT-2** model for generating responses to user queries.
- **Symptom-based Advice:** Provides helpful advice based on commonly asked questions like fever, cough, diabetes, stress, and more.
- **User Feedback:** After interacting with the chatbot, users can provide feedback about the response, allowing the system to improve.
- **Suggestion Box:** In case the response is unhelpful, users can submit suggestions for improvement.

## Technologies Used

- **Streamlit:** For building the user interface and deploying the chatbot application.
- **Transformers:** For accessing and utilizing pre-trained language models like **DistilGPT-2**.
- **TensorFlow:** For machine learning model inference (though the current model is based on PyTorch, TensorFlow is used in some parts of the development for potential future integration).
- **NLTK:** For natural language processing tasks such as text processing and tokenization.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository:

git clone https://github.com/RimshaTahreem/AI-Powered_Health_Assistant
cd healthcare-chatbot
```

### 2. Install dependencies:
Ensure you have Python installed.


pip install -r requirements.txt
```

### 3. Run the application:

streamlit run app.py
```

### 4. Access the chatbot in your browser:
The Streamlit app will open in your default browser at `http://localhost:8501/`.

## Project Structure

- `app.py`: Main application file that handles the chatbot interface and logic.
- `requirements.txt`: List of Python dependencies required for the project.
- `assets/`: Folder for storing any images or assets used in the project.
- `README.md`: Documentation for the project.

## How It Works

1. **User Input:** The user types a query or health-related question in the input box.
2. **Response Generation:** The chatbot checks if the query matches predefined keywords (like "fever," "cough," etc.). If so, it provides a specific health tip. Otherwise, it generates a response using the **DistilGPT-2** model.
3. **User Feedback:** After the chatbot responds, the user can rate the response by selecting "Yes" or "No" for helpfulness.
4. **Suggestions:** If the user selects "No," a suggestion box appears, allowing the user to submit feedback on how the response can be improved.
5. **Thank You Message:** When the user submits feedback, the chatbot thanks them for their input.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
