# Load documents
from rag.loader import load_documents


def retrieve_document(question):

    # Load knowledge base documents
    documents = load_documents()

    # Convert question into lowercase words
    question_words = question.lower().split()

    scores = {}

    # Compare question with each document
    for doc_name, content in documents.items():

        document_words = content.lower().split()

        score = 0

        # Count matching words
        for word in question_words:

            score += document_words.count(word)

        scores[doc_name] = score

    # Return document with highest score
    best_document = max(
        scores,
        key=scores.get
    )

    return best_document


if __name__ == "__main__":

    question = "How do I reset my password?"

    result = retrieve_document(question)

    print("Question:")
    print(question)

    print("\nRetrieved Document:")
    print(result)