# Chatbot using OpenAI GPT-3.5 and Flask

This is a simple chatbot application built using Flask and OpenAI's GPT-3.5 model.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/chatbot.git
    cd chatbot
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install flask
    pip install openai
    ```

4. **Create a `config.py` file**:
    ```sh
    echo "OPENAI_KEY = 'your-openai-key-here'" > config.py
    ```

## Usage

1. **Run the app**:
    ```sh
    python huggingfacechatbot.py
    ```

2. **Access the chatbot**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

## API Endpoints

- **Serve the index page**:
    ```
    GET /
    ```

- **Serve static files**:
    ```
    GET /<path:path>
    ```

- **Chatbot interaction**:
    ```
    POST /chatbot
    ```

    **Request Body**:
    ```json
    {
        "message": "Your message here"
    }
    ```

    **Response**:
    ```json
    {
        "message": "Chatbot's response"
    }
    ``
