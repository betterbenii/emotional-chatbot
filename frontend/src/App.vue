<template>
  <div class="app">
    <ChatWindow :messages="messages" @send-message="handleSendMessage" />
    <EmotionSliders @update-parameters="handleParameterUpdate" />
    <InstructionSidebar />
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue';
import EmotionSliders from './components/EmotionSliders.vue';
import api from './services/api';
import InstructionSidebar from './components/InstructionSidebar.vue';

export default {
  components: {
    ChatWindow,
    EmotionSliders,
    InstructionSidebar,
  },
  /**
   * Conversation history. Each message is an object with
   * { role: 'assistant' | 'user', content: string }.
   *
   * @type {{ role: string, content: string }[]}
   */
  data() {
    return {
      messages: [
        { role: 'assistant', content: 'Hello! How can I help you today?' },
      ],
    };
  },
  methods: {
    /**
     * Handle user message input by adding it to the conversation history
     * and sending it to the chatbot API for a response.
     *
     * @param {string} message - The user's message
     */
    async handleSendMessage(message) {
      this.messages.push({ role: 'user', content: message });

      try {
        const response = await api.sendMessage(message);
        const chatbotResponse = response.data.response;
        this.messages.push({ role: 'assistant', content: chatbotResponse });
      } catch (error) {
        console.error('Error sending message:', error);
        this.messages.push({ role: 'assistant', content: 'Sorry, something went wrong.' });
      }
    },
    /**
     * Update the chatbot's emotional parameters and try to adjust the parameters
     * using the API.
     *
     * @param {Object} parameters - The new emotional parameters for the chatbot
     */
    async handleParameterUpdate(parameters) {
      try {
        await api.adjustParameters(parameters);
        console.log('Parameters updated successfully');
      } catch (error) {
        console.error('Error updating parameters:', error);
      }
    },
  },
};
</script>

<style>
.app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;

}

.chat-container {
  flex: 1;
  padding-right: 320px; /* Leaves space for sidebar */
}
</style>