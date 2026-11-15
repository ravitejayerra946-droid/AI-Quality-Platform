# Import RAG generator
from rag.generator import generate_answer


def test_rag_pipeline():

    question = (
        "How do I reset my password?"
    )

    result = generate_answer(question)

    # Verify correct document retrieved
    assert (
        result["document"]
        == "password_policy.txt"
    )

    # Verify answer exists
    assert (
        len(result["answer"]) > 0
    )