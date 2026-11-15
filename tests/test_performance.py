# Used to measure execution time
import time

# Import RAG pipeline
from rag.generator import generate_answer


def test_rag_response_time():

    # Start timer
    start_time = time.time()

    # Run complete RAG flow
    result = generate_answer(
        "How do I reset my password?"
    )

    # Stop timer
    end_time = time.time()

    latency = end_time - start_time

    print(
        f"\nLatency: {latency:.2f} seconds"
    )

    # Verify correct document
    assert (
        result["document"]
        == "password_policy.txt"
    )

    # Performance Quality Gate
    assert latency < 10