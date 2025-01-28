<template>
  <div class="app">
    <ChatWindow :messages="messages" @send-message="handleSendMessage" />
    <EmotionSliders @update-parameters="handleParameterUpdate" />
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue';
import EmotionSliders from './components/EmotionSliders.vue';
import api from './services/api';

export default {
  components: {
    ChatWindow,
    EmotionSliders,
  },
  data() {
    return {
      messages: [
        { role: 'assistant', content: 'Hello! How can I help you today?' },
      ],
    };
  },
  methods: {
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
</style>