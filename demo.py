import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain


def create_llm_chain(model_name, temperature, max_tokens, index_path, request_timeout=10, max_retries=2):
    if model_name == "gpt-3.5-turbo":
        llm = ChatOpenAI(
            temperature=temperature,
            model_name=model_name,
            max_tokens=max_tokens,
            request_timeout=request_timeout,
            max_retries=max_retries
        )
    else:
        llm = OpenAI(
            temperature=temperature,
            model_name=model_name,
            max_tokens=max_tokens,
            request_timeout=request_timeout,
            max_retries=max_retries
        )

    embeddings = OpenAIEmbeddings()
    faiss_index = FAISS.load_local(index_path, embeddings)

    llm_chain = ConversationalRetrievalChain.from_llm(
        llm, faiss_index.as_retriever(), max_tokens_limit=1024
    )

    return llm_chain


def ask_ai_interactive(llm_chain):
    chat_history = []
    print("Welcome to the Personal Assistant! Type 'exit' to stop.")
    while True:
        query = input("Please enter your question: ")

        if query.lower() == "exit":
            break

        result = llm_chain({"question": query, "chat_history": chat_history})
        chat_history.append((query, result["answer"]))

        print("Answer:", result["answer"])


if __name__ == "__main__":
    load_dotenv()
    llm_chain = create_llm_chain(
        model_name=os.getenv("LLM_NAME"),
        temperature=os.getenv("LLM_TEMPERATURE"),
        max_tokens=os.getenv("LLM_MAX_TOKENS"),
        index_path=os.getenv("FAISS_INDEX_PATH"),
    )
    ask_ai_interactive(llm_chain)
