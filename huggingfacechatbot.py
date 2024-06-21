from openai import OpenAI
from flask import Flask, request, jsonify, send_from_directory
from config import OPENAI_KEY

app = Flask(__name__)

# Set your OpenAI API key here
client = OpenAI(api_key=OPENAI_KEY)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('static', path)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data['message']

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        chatbot_response = response.choices[0].message.content
    except Exception as e:
        chatbot_response = str(e)

    return jsonify({"message": chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
