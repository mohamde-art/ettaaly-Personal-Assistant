# ettaaly Personal Assistant 🤖

ettaaly Personal Assistant is an interactive chatbot web application built with **Streamlit** and **LangChain**, powered by **OpenAI GPT-3.5 Turbo**.  
It allows users to ask questions, and the assistant responds intelligently by retrieving information from a provided text document (`data.txt`).

---

## 🚀 Features

- **Interactive Chat Interface**  
  Friendly chat bubbles with avatars for user and bot using `streamlit-chat`.

- **Conversational Memory**  
  Remembers previous interactions during the session for context-aware responses.

- **Document-Based Answers**  
  Retrieves information from a custom text file (`data.txt`) and integrates it into GPT responses.

- **Custom Styling**  
  Rounded input boxes, custom buttons, and a clean chat layout.

---

## 🛠️ Technologies

- Python 3.x  
- Streamlit  
- streamlit-chat  
- LangChain  
- OpenAI API  

---

## 📂 Project Structure
ettaaly-Personal-Assistant/
│── chatbot.py # Main application
│── data.txt # Knowledge base for the assistant
│── README.md # Project documentation
│── requirements.txt # Python dependencies

---

## 📖 Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/ettaaly-Personal-Assistant.git
cd ettaaly-Personal-Assistant
pip install -r requirements.txt
streamlit run chatbot.py

