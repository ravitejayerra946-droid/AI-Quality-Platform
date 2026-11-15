# Read CSV dataset
import pandas as pd

# Build safe file paths
from pathlib import Path

# Import retriever
from rag.retriever import retrieve_document


def test_retrieval_accuracy():

    # Path to golden dataset
    dataset_path = (
        Path(__file__).parent.parent
        / "data"
        / "evaluation_dataset.csv"
    )

    # Read CSV
    dataset = pd.read_csv(dataset_path)

    # Loop through test cases
    for row in dataset.itertuples(index=False):

        question = row.question

        expected_document = row.expected_document

        # Run retriever
        retrieved_document = retrieve_document(
            question
        )

        # Verify result
        assert (
            retrieved_document
            == expected_document
        ), (
            f"Expected "
            f"{expected_document}, "
            f"but got "
            f"{retrieved_document}"
        )