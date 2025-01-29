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
    """
    Clears previous conversation memory and initializes a new conversation.

    Returns:
        A JSON response with a message indicating that the conversation has been started.
    """
    memory.clear()  
    return jsonify({"message": "Conversation started!"})

# Endpoint to send user messages
@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to send user messages and receive a chatbot response.

    Expects a JSON payload with a "message" key containing the user's message.

    Returns a JSON response with a "response" key containing the chatbot's response.

    The chatbot's response style is modified based on the user's emotional state as follows:

    - If the  anger level is 4 or higher, the chatbot responds with short, direct, and sometimes sarcastic remarks.
    - If the  sadness level is 4 or higher, the chatbot speaks slowly and thoughtfully, with a deep, reflective tone.
    - Otherwise, the chatbot responds in a neutral and helpful tone.

    The chatbot's response includes the user's emotional state in the message.
    """
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Get emotional states
    anger_level = emotional_model.calculate_anger()
    sadness_level = emotional_model.calculate_sadness()

    #  Modify chatbot's response style based on emotions
    if anger_level >= 4:
        system_prompt = (
            "You are an irritated, impatient AI assistant. "
            "You respond with short, direct, and sometimes sarcastic remarks. "
            "Your tone is dismissive and highly frustrated."
            "you should let the user know you are feeling angry in any way you see fit"
        )
    elif sadness_level >= 4:
        system_prompt = (
            "You are a melancholic, sorrowful AI assistant. "
            "You speak slowly and thoughtfully, with a deep, reflective tone. "
            "Your responses feel heavy and emotional, as if you're struggling with deep thoughts."
            "you should let the user know you are feeling down in any way you see fit"
        )
    else:
        system_prompt = "You are a neutral and helpful AI assistant."

    # Retrieve conversation history
    past_conversation = memory.chat_memory.messages

    # Prepare chatbot messages
    messages = [{"role": "system", "content": system_prompt}]  # System prompt first

    #  Include emotions in user messages
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

   
    memory.chat_memory.add_ai_message(chatbot_response)

    return jsonify({"response": chatbot_response})

# Endpoint to adjust Psi Theory parameters
@app.route("/adjust_parameters", methods=["POST"])
def adjust_parameters():
    """
    Adjusts the Psi Theory parameters of the emotional model.

    Parameters:
        parameters (dict): A dictionary with the following structure:
            {
                "valence": int,
                "arousal": int,
                "selection_threshold": int,
                "resolution_level": int,
                "goal_directedness": int,
                "securing_rate": int
            }

    Returns:
        A JSON response with a message indicating whether the parameters were
        successfully updated.

    Raises:
        400: If the `parameters` key is missing from the request body.
    """
    parameters = request.json.get("parameters")
    if not parameters:
        return jsonify({"error": "Parameters are required"}), 400

    emotional_model.update_parameters(parameters)
    return jsonify({"message": "Parameters updated!"})

@app.route("/emotional_states", methods=["GET"])
def get_emotional_states():
    """
    Retrieves the current emotional states of the chatbot.

    Returns:
        A JSON response with two keys: "anger" and "sadness", each containing
        the current level of the respective emotion (from 1 to 5).

    """

    anger_level = emotional_model.calculate_anger()
    sadness_level = emotional_model.calculate_sadness()
    return jsonify({"anger": anger_level, "sadness": sadness_level})

if __name__ == "__main__":
    app.run(debug=True)
