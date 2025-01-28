import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Backend URL
});

export default {
  startConversation() {
    return api.post('/start');
  },
  sendMessage(message) {
    return api.post('/chat', { message });
  },
  adjustParameters(parameters) {
    return api.post('/adjust_parameters', { parameters });
  },
  getEmotionalStates() {
    return api.get('/emotional_states');
  },
};