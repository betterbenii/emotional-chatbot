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