# Emotional AI Chatbot Using Dorner’s Psi Theory

## **Project Overview**
This project is an **emotional AI chatbot** that dynamically adapts its responses based on **Dorner's Psi Theory**. The chatbot calculates and reflects **anger and sadness** levels, adjusting its dialogue accordingly. Users can modify emotional parameters mid-conversation through an intuitive **Vue.js frontend**, while the chatbot's logic and memory management are handled using **Flask & LangChain**.

---

## **Features & Functionalities**
✅ **Adjustable Emotional Parameters**: Users can control **valence, arousal, selection threshold, resolution level, goal-directedness, and securing rate** via sliders.  
✅ **Real-Time Emotion Calculation**: The chatbot dynamically calculates **anger and sadness levels**.  
✅ **Adaptive Dialogue**: Responses vary based on emotions (e.g., anger results in assertiveness, sadness leads to melancholic responses).  
✅ **Memory Persistence**: Chatbot retains conversation history even when emotions are adjusted.  
✅ **Seamless UI**: Vue.js frontend for an intuitive experience.  

---

## **Technology Stack**
- **Frontend**: Vue.js (Vue CLI, Axios)
- **Backend**: Flask, LangChain, Groq API
- **Memory Management**: LangChain's `ConversationBufferMemory`
- **Environment Variables**: `.env` file for API keys & configuration

---

## **Project Structure**
```
EmotionalAI-Chatbot/
│── backend/
│   ├── venv/                    # Virtual environment (Flask backend)
│   ├── .env                     # Environment variables (GROQ_API_KEY)
│   ├── app.py                   # Flask API for chatbot
│   ├── emotional_model.py        # Emotion calculation logic
│── frontend/
│   ├── src/
│   │   ├── assets/               # Static assets
│   │   ├── components/           # Vue.js UI components
│   │   │   ├── ChatWindow.vue    # Chatbot UI
│   │   │   ├── EmotionSlider.vue # Emotion adjustment sliders
│   │   │   ├── InstructionSidebar.vue  # Sidebar with chatbot instructions
│   │   ├── services/             # API interaction logic
│   │   ├── App.vue               # Main Vue app file
│   │   ├── main.js               # Vue.js entry file
│   ├── public/
│   ├── package.json              # Frontend dependencies
│── README.md
```

---

## **Installation & Setup**

### **1️⃣ Backend Setup (Flask)**
1. **Clone the repository:**
   ```sh
   git clone <repo-link>
   cd backend
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate # For macOS/Linux
   ```
3. **Install dependencies:**
  
4. **Set up environment variables:**
   - Create a `.env` file in the `backend/` folder.
   - Add the following line:
     ```sh
     GROQ_API_KEY=your-api-key-here
     ```
5. **Run the Flask backend:**
   ```sh
   python app.py
   ```

### **2️⃣ Frontend Setup (Vue.js)**
1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Run the Vue development server:**
   ```sh
   npm run serve
   ```
4. **Open the application in your browser:**
   - Go to `http://localhost:8080`

---

## **How to Use the Chatbot**
1. **Start the Flask backend** (`python app.py`).
2. **Run the Vue frontend** (`npm run serve`).
3. **Adjust emotional parameters** using the sliders.
4. **Type messages** in the chat window to interact with the chatbot.
5. **Observe how emotions affect responses** (high anger → assertive, high sadness → melancholic).
6. **Modify emotions anytime** without losing conversation history.


---

## **Understanding the Emotional Model**
The chatbot follows **Dorner’s Psi Theory**, adapting its behavior based on **six key parameters**:
- **Valence Level**: Determines positivity or negativity.
- **Arousal Level**: Readiness for action.
- **Selection Threshold**: Stability in decision-making.
- **Resolution Level**: Accuracy of perception.
- **Goal-Directedness**: Focus on achieving objectives.
- **Securing Rate**: Frequency of environmental checks.

### **Emotion Calculation**
- **Anger**: High arousal + negative valence + high selection threshold.
- **Sadness**: Low arousal + negative valence + low goal-directedness.

The chatbot **dynamically adjusts its tone** based on these calculations:
- **High Anger** → Short, assertive, impatient responses.
- **High Sadness** → Slow, melancholic, thoughtful responses.

---

## **Troubleshooting & FAQs**
### **1. The chatbot is not responding.**
✅ Ensure the **Flask backend is running** (`python app.py`).  
✅ Check if the **Vue frontend is running** (`npm run serve`).  
✅ Open Developer Console (`F12`) and check for errors.  
✅ Confirm the **GROQ_API_KEY** is set in `.env`.

### **2. I get a CORS error.**
✅ Restart the Flask backend. Ensure `flask_cors` is installed and enabled in `app.py`.

### **3. How do I reset the chatbot’s memory?**
✅ Click the "Start Over" button in the UI.
✅ Or manually restart the Flask backend.

---

## **Contributors & Credits**
- **Developer:** Abenezer Temesgen

- **Technologies Used:** Vue.js, Flask, LangChain, Groq API

🚀 **Enjoy experimenting with AI emotions!** 🚀

