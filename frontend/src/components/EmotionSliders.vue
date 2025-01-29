<template>
    <div class="sliders">
      <h2>Adjust Emotional Parameters</h2>
      <div v-for="(value, key) in parameters" :key="key" class="slider">
        <label>{{ key }}</label>
        <input
          type="range"
          :min="1"
          :max="7"
          :value="value"
          @input="updateParameter(key, $event.target.value)"
        />
        <span>{{ value }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    /**
     * Initial emotional parameters for the chatbot, with values ranging from 1 (extremely low) to 7 (extremely high).
     * The parameters are:
     * - valence: Measures the chatbot's emotional valence on a scale from extremely negative (1) to extremely positive (7).
     * - arousal: Represents the chatbot's physiological arousal level, ranging from extremely low (1) to extremely high (7).
     * - selection threshold: The minimum value required for the chatbot to make a decision, from extremely low (1) to extremely high (7).
     * - resolution level: The chatbot's ability to distinguish between different objects, ranging from extremely low (1) to extremely high (7).
     * - goal-directedness: The chatbot's motivation to achieve goals, ranging from extremely low (1) to extremely high (7).
     * - securing rate: The chatbot's ability to secure resources, ranging from extremely low (1) to extremely high (7).
     * @type {Object}
     * @property {number} valence
     * @property {number} arousal
     * @property {number} selection_threshold
     * @property {number} resolution_level
     * @property {number} goal_directedness
     * @property {number} securing_rate
     */
    data() {
      return {
        parameters: {
          valence: 4,
          arousal: 4,
          selection_threshold: 4,
          resolution_level: 4,
          goal_directedness: 4,
          securing_rate: 4,
        },
      };
    },
    methods: {
/**
 * Updates a specific emotional parameter and emits an event.
 *
 * @param {string} key - The key of the parameter to update.
 * @param {number|string} value - The new value for the parameter, which will be
 *                                converted to a number.
 *
 * Emits:
 * @event update-parameters - Emitted with the updated parameters object.
 */

      updateParameter(key, value) {
        this.parameters[key] = Number(value);
        this.$emit('update-parameters', this.parameters);
      },
    },
  };
  </script>
  
  <style>
  .sliders {
    margin-top: 20px;
    padding: 16px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }
  
  .slider {
    margin-bottom: 12px;
  }
  
  .slider label {
    display: block;
    margin-bottom: 4px;
    font-weight: bold;
  }
  
  .slider input {
    width: 100%;
  }
  
  .slider span {
    display: inline-block;
    margin-left: 8px;
  }
  </style>