<template>
    <div class="sidebar">
      <h2>Chatbot Instructions</h2>
      
      <h3>How Emotions Are Calculated</h3>
      <p>
        The chatbot uses <strong>Dörner’s Psi Theory</strong> to determine emotional states:
      </p>
      <ul>
        <li><strong>Anger:</strong> Increases when obstacles prevent goal achievement.</li>
        <li><strong>Sadness:</strong> Rises when no clear solutions are available.</li>
        <li>Other factors like <em>arousal, selection threshold, and securing rate</em> also influence emotions.</li>
      </ul>
  
      <h3>How to Use</h3>
      <ol>
        <li>Adjust the <strong>emotional sliders</strong> to influence the chatbot’s mood.</li>
        <li><strong>Anger formula: high arousal + negative valence + high selection threshold </strong></li>
        <li><strong>Sadness formula: low arousal + negative valence + low goal-directedness</strong></li>
        <li>Start a conversation by typing a message.</li>
        <li>If anger is high, the bot will respond assertively.</li>
        <li>If sadness is high, the bot will sound melancholic.</li>
        
      </ol>
  
      <h3>Tips</h3>
      <p>
        Try different emotional settings to see how the chatbot reacts! 
        A mix of high sadness and high anger creates a different personality.
      </p>
    </div>
  </template>
  
  <style scoped>
  .sidebar {
    width: 300px;
    height: 100vh;
    position: fixed;
    right: 0;
    top: 0;
    background-color: #f8f9fa;
    padding: 20px;
    box-shadow: -3px 0 5px rgba(0, 0, 0, 0.1);
    overflow-y: auto;
  }
  
  h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
  }
  
  h3 {
    font-size: 1.2rem;
    margin-top: 15px;
  }
  
  ul, ol {
    padding-left: 20px;
  }
  
  p {
    font-size: 0.95rem;
  }
  </style>
  