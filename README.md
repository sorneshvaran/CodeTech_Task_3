# 🤖 Task 3: Rule-Based Chatbot using NLP (Python)

This repository contains **Task 3** from my CodeTech internship, where I built a simple **rule-based chatbot** using Python and basic Natural Language Processing (NLP). The bot matches user input to pre-defined intents using string similarity and basic preprocessing techniques.

---

## 📌 Project Objective

- To create a chatbot that can respond to user queries.
- To handle basic NLP tasks like tokenization and preprocessing.
- To use intent-matching logic with a confidence threshold.
- To organize the code into a modular structure.

---

## 🛠️ Tools & Technologies Used

- `Python 3.x`
- `json` (for storing patterns and responses)
- `string`, `re` (for preprocessing)
- Custom modules: `intent_match.py`, `preprocess.py`

---

## 📁 Project Structure

```bash
📦 Chatbot_Project
 ┣ 📄 main.py
 ┣ 📄 intent_match.py
 ┣ 📄 preprocess.py
 ┣ 📄 responses.json
 ┗ 📄 README.md
````

---

## 💡 How It Works

1. Loads predefined user patterns and responses from `responses.json`.
2. Preprocesses both patterns and user input using `preprocess.py`.
3. Matches user input to closest intent using a similarity score in `intent_match.py`.
4. Returns the best-matched response if confidence is ≥ 0.3; otherwise, returns a default fallback.

---

## 🔧 How to Run the Chatbot

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Chatbot_Project.git
   cd Chatbot_Project
   ```

2. **Ensure the required files exist**

   * `main.py`
   * `intent_match.py`
   * `preprocess.py`
   * `responses.json`

3. **Run the chatbot**

   ```bash
   python main.py
   ```

4. **Interact**

   * Type messages to the chatbot.
   * Type `bye`, `exit`, or `quit` to end the conversation.

---

## ✨ Features

* Rule-based matching with adjustable confidence threshold
* Preprocessing using stopword removal, lemmatization, and punctuation filtering
* Modular code for easy scaling and maintenance

---

## 🏁 Learning Outcomes

* How to build a basic NLP-based chatbot.
* Text preprocessing using Python libraries.
* Intent matching using cosine similarity or custom logic.
* Reading and writing JSON data.
