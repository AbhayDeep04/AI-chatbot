from openai import OpenAI
from flask import Flask, request, jsonify, send_from_directory
from config import OPENAI_KEY

app = Flask(__name__)

# Set your OpenAI API key here
client = OpenAI(api_key=OPENAI_KEY)

# Initialize an empty list to store the conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('static', path)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global conversation_history

    data = request.get_json()
    user_message = data['message']

    # Append the user message to the conversation history
    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        chatbot_response = response.choices[0].message.content

        # Append the chatbot response to the conversation history
        conversation_history.append({"role": "assistant", "content": chatbot_response})
    except Exception as e:
        chatbot_response = str(e)

    return jsonify({"message": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
