<template>
    <div class="chat-window">
      <div class="messages">
        <div v-for="(message, index) in messages" :key="index" :class="['message', message.role]">
          {{ message.content }}
        </div>
      </div>
      <div class="input-area">
        <input
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Type a message..."
        />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      messages: {
        type: Array,
        required: true,
      },
    },
/**
 * Provides component-specific reactive data properties.
 *
 * @returns {Object} An object containing:
 *   - newMessage: {string} A string to hold the current input message from the user.
 */

    data() {
      return {
        newMessage: '',
      };
    },
    methods: {
      /**
       * Emits a "send-message" event with the current input message to the parent
       * component when the user presses Enter or clicks the Send button.
       *
       * Clears the input message text after sending.
       */
      sendMessage() {
        if (this.newMessage.trim()) {
          this.$emit('send-message', this.newMessage);
          this.newMessage = '';
        }
      },
    },
  };
  </script>
  
  <style>
  .chat-window {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    background-color: #f9f9f9;
  }
  
  .messages {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 16px;
  }
  
  .message {
    padding: 8px;
    margin-bottom: 8px;
    border-radius: 4px;
  }
  
  .message.user {
    background-color: #007bff;
    color: white;
    align-self: flex-end;
  }
  
  .message.assistant {
    background-color: #e9ecef;
    color: black;
    align-self: flex-start;
  }
  
  .input-area {
    display: flex;
    gap: 8px;
  }
  
  .input-area input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .input-area button {
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .input-area button:hover {
    background-color: #0056b3;
  }
  </style>