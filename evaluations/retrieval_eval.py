# Helps build file paths safely
from pathlib import Path

# Reads CSV files
import pandas as pd

# Import retriever
from rag.retriever import retrieve_document


def evaluate_retrieval():

    # Build path to evaluation dataset
    dataset_path = (
        Path(__file__).parent.parent
        / "data"
        / "evaluation_dataset.csv"
    )

    print("Reading dataset from:")
    print(dataset_path)

    # Read CSV
    dataset = pd.read_csv(dataset_path)

    print("\nDataset Loaded:")
    print(dataset)

    print("\nColumns:")
    print(dataset.columns)

    print("\nTotal Rows:")
    print(len(dataset))

    total_questions = 0
    correct_retrievals = 0

    # Loop through each row
    for row in dataset.itertuples(index=False):

        question = row.question
        expected_document = row.expected_document

        retrieved_document = retrieve_document(
            question
        )

        print("\n" + "=" * 50)

        print("Question:")
        print(question)

        print("\nExpected Document:")
        print(expected_document)

        print("\nRetrieved Document:")
        print(retrieved_document)

        total_questions += 1

        if retrieved_document == expected_document:

            print("\nResult: PASS")

            correct_retrievals += 1

        else:

            print("\nResult: FAIL")

    print("\n" + "=" * 50)

    print("Correct Retrievals:", correct_retrievals)
    print("Total Questions:", total_questions)

    # Prevent division by zero
    if total_questions == 0:

        print(
            "\nNo questions found in dataset."
        )

        return

    accuracy = (
        correct_retrievals /
        total_questions
    ) * 100

    print(
        f"\nRetrieval Accuracy: "
        f"{accuracy:.2f}%"
    )


if __name__ == "__main__":

    evaluate_retrieval()
