import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Backend URL
});

export default {
  /**
   * Clears previous conversation memory and initializes a new conversation.
   *
   * Returns a JSON response with a message indicating that the conversation has been started.
   */
  startConversation() {
    return api.post('/start');
  },
  /**
   * Sends a message to the chatbot and retrieves its response.
   *
   * @param {string} message - The user's message to the chatbot.
   *
   * @returns {Promise<Object>} A JSON response containing the chatbot's response.
   */
  sendMessage(message) {
    return api.post('/chat', { message });
  },
  /**
   * Adjusts the chatbot's emotional parameters via the API.
   *
   * @param {Object} parameters - A dictionary containing the new values for the emotional parameters.
   *
   * @returns {Promise<Object>} A JSON response indicating whether the parameters were successfully updated.
   */

  /**
   * Adjusts the chatbot's emotional parameters via the API.
   *
   * @param {Object} parameters - A dictionary containing the new values for the emotional parameters.
   *
   * @returns {Promise<Object>} A JSON response indicating whether the parameters were successfully updated.
   */
  adjustParameters(parameters) {
    return api.post('/adjust_parameters', { parameters });
  },
  /**
   * Retrieves the current emotional states of the chatbot.
   *
   * Returns a JSON response with two keys: "anger" and "sadness", each containing
   * the current level of the respective emotion (from 1 to 5).
   */
  getEmotionalStates() {
    return api.get('/emotional_states');
  },
};