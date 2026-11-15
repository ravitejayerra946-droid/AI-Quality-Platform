# Read environment variables
import os

# Load .env
from dotenv import load_dotenv

# Groq SDK
from groq import Groq

# Import retriever
from rag.retriever import retrieve_document

# Import loader
from rag.loader import load_documents


# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

print("API Key Loaded:", bool(api_key))

# Create Groq client
client = Groq(
    api_key=api_key
)


def generate_answer(question):

    # Step 1
    # Retrieve most relevant document
    document_name = retrieve_document(
        question
    )

    # Step 2
    # Load all documents
    documents = load_documents()

    # Step 3
    # Get selected document content
    context = documents[document_name]

    # Step 4
    # Build grounded prompt

    prompt = f"""
You are a company assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    # Step 5
    # Ask Groq LLM

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    # Step 6
    # Return everything useful for evaluation

    return {
        "question": question,
        "document": document_name,
        "context": context,
        "answer":
            response.choices[0]
            .message.content
    }


# Test run
if __name__ == "__main__":

    result = generate_answer(
        "How do I reset my password?"
    )

    print("\nQuestion:")
    print(result["question"])

    print("\nRetrieved Document:")
    print(result["document"])

    print("\nAnswer:")
    print(result["answer"])