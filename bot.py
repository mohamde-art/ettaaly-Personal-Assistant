import os
import streamlit as st
from streamlit_chat import message
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
import warnings

warnings.filterwarnings("ignore")

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="ettaaly Personal Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------- Sidebar -------------------
with st.sidebar:
    st.header("Settings")
    model_choice = st.selectbox("Choose GPT model:", ["gpt-3.5-turbo", "gpt-4"])
    k_value = st.slider("Number of retrieved documents (k):", 1, 5, 1)
    st.write("---")
    st.markdown("ettaaly Personal Assistant v1.0")

# ------------------- Custom CSS -------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #f0f4ff, #d9e8ff);
}
.stTextInput input {
    border-radius: 12px;
    padding: 10px;
}
.stButton button {
    border-radius: 10px;
    background-color: #007bff;
    color: white;
    padding: 8px 16px;
}
.stButton button:hover {
    background-color: #0056b3;
    color: white;
}
.user-message {
    background-color: #007bff;
    color: white;
    padding: 12px;
    border-radius: 15px;
    margin: 5px 0;
    max-width: 70%;
}
.bot-message {
    background-color: #e5e5e5;
    padding: 12px;
    border-radius: 15px;
    margin: 5px 0;
    max-width: 70%;
}
</style>
""", unsafe_allow_html=True)

# ------------------- Title -------------------
st.markdown("<h2 style='text-align: center; color: #007bff;'>📚 ettaaly Books - Personal Assistant 🤖</h2>", unsafe_allow_html=True)
st.write("---")

# ------------------- Containers -------------------
request_container = st.container()
response_container = st.container()

# ------------------- Data Loading -------------------
data_file = "data.txt"
loader = TextLoader(data_file, encoding='utf-8')
loader.load()

index = VectorstoreIndexCreator(
    embedding=OpenAIEmbeddings()
).from_loaders([loader])

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model=model_choice),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": k_value})
)

# ------------------- Session State -------------------
if "history" not in st.session_state:
    st.session_state["history"] = []

if "generated" not in st.session_state:
    st.session_state["generated"] = ["Hello 👋! I am your Personal assistant built by ettaaly Books Store"]

if "past" not in st.session_state:
    st.session_state["past"] = ["Hey there!"]

# ------------------- Chat Function -------------------
def conversational_chat(prompt):
    result = chain({"question": prompt, "chat_history": st.session_state["history"]})
    st.session_state["history"].append((prompt, result["answer"]))
    return result["answer"]

# ------------------- Input -------------------
with request_container:
    with st.form(key="chat_form", clear_on_submit=True):
        cols = st.columns([8, 2])
        with cols[0]:
            user_input = st.text_input("💬 Type your message:", placeholder="Message ettaalyBot...", key="input")
        with cols[1]:
            submit_button = st.form_submit_button(label="🚀 Send")

    if submit_button and user_input:
        with st.spinner("ettaalyBot is typing..."):
            output = conversational_chat(user_input)
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)

# ------------------- Chat History -------------------
if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"])):
            message(
                st.session_state["past"][i],
                is_user=True,
                key=str(i) + "_user",
                avatar_style="adventurer",
                seed=13
            )
            message(
                st.session_state["generated"][i],
                key=str(i),
                avatar_style="bottts",
                seed=2
            )
