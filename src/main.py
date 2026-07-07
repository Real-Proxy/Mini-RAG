from ingest import ingest_documents
from query import ask_question

def main():
    ingest_documents(["Uploads/ArchitMishra_Resume.pdf"])

    while True:
        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        answer = ask_question(query)

        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()