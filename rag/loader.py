# Path helps us work with file and folder locations
from pathlib import Path


# Function to load all text documents from the knowledge base
def load_documents():

    # Empty dictionary to store documents
    documents = {}

    # Path to knowledge base documents
    docs_path = (
        Path(__file__).parent.parent
        / "data"
        / "documents"
    )

    # Find all text files
    files = list(
        docs_path.glob("*.txt")
    )

    # Read each document
    for file in files:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            documents[file.name] = (
                f.read()
            )

    return documents


# Run only when executing loader.py directly
if __name__ == "__main__":

    docs = load_documents()

    print(
        f"\nTotal documents loaded: "
        f"{len(docs)}"
    )

    for name, content in docs.items():

        print(f"\n{name}")

        print("-" * 50)

        print(content)