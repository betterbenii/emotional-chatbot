from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain.memory import ConversationBufferMemory
from groq import Groq
from dotenv import load_dotenv
import os
from emotional_model import emotional_model

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Groq Client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize LangChain memory
memory = ConversationBufferMemory()

# Endpoint to start a conversation
@app.route("/start", methods=["POST"])
def start_conversation():
    memory.clear()  # Clear previous conversation memory
    return jsonify({"message": "Conversation started!"})

# Endpoint to send user messages
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Get emotional states
    anger_level = emotional_model.calculate_anger()
    sadness_level = emotional_model.calculate_sadness()

    # Modify chatbot's emotional tone 
    if anger_level >= 4:
        system_prompt = "You are an irritated and impatient assistant. Respond in a short, frustrated tone."
    elif sadness_level >= 4:
        system_prompt = "You are a sad and melancholic assistant. Respond in a slow, sorrowful manner."
    else:
        system_prompt = "You are a helpful and neutral assistant."

    # Retrieve conversation history
    past_conversation = memory.chat_memory.messages

    # Prepare chatbot messages
    messages = [{"role": "system", "content": system_prompt}]  # System prompt first

    # Append past messages
    for msg in past_conversation:
        role = "user" if msg.type == "human" else "assistant"
        messages.append({"role": role, "content": msg.content})

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    # Get chatbot response using Groq
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="mixtral-8x7b-32768",
    )

    # Extract chatbot response
    chatbot_response = chat_completion.choices[0].message.content

    # Add chatbot response to memory
    memory.chat_memory.add_ai_message(chatbot_response)

    return jsonify({"response": chatbot_response})

# Endpoint to adjust Psi Theory parameters
@app.route("/adjust_parameters", methods=["POST"])
def adjust_parameters():
    parameters = request.json.get("parameters")
    if not parameters:
        return jsonify({"error": "Parameters are required"}), 400

    emotional_model.update_parameters(parameters)
    return jsonify({"message": "Parameters updated!"})

@app.route("/emotional_states", methods=["GET"])
def get_emotional_states():
    anger_level = emotional_model.calculate_anger()
    sadness_level = emotional_model.calculate_sadness()
    return jsonify({"anger": anger_level, "sadness": sadness_level})

if __name__ == "__main__":
    app.run(debug=True)
