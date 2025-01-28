from flask import Flask, request, jsonify
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from groq import Groq
from dotenv import load_dotenv
import os
from emotional_model import emotional_model

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize LangChain memory
memory = ConversationBufferMemory()


# conversation = ConversationChain(llm=llm, memory=memory)

# Endpoint to start a conversation
@app.route("/start", methods=["POST"])
def start_conversation():
    memory.clear()  # Clear previous conversation memory
    return jsonify({"message": "Conversation started!"})

# Endpoint to send user messages
@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Add user message to memory
    memory.chat_memory.add_user_message(user_message)

    # Get emotional states
    anger_level = emotional_model.calculate_anger()
    sadness_level = emotional_model.calculate_sadness()

    # Modify system prompt based on emotional state
    system_prompt = "You are a helpful assistant."
    if anger_level >= 4:
        system_prompt = "You are feeling angry. Respond assertively."
    elif sadness_level >= 4:
        system_prompt = "You are feeling sad. Respond empathetically."

    # Get chatbot response using Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        model="mixtral-8x7b-32768",  # Replace with your preferred Groq model
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