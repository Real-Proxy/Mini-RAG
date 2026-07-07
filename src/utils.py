from langchain_community.document_loaders import TextLoader, PyPDFLoader


def load_document(file_path):
    """
    Loads a TXT or PDF document based on its extension.
    """

    if file_path.lower().endswith(".txt"):
        loader = TextLoader(file_path)

    elif file_path.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    return loader.load()