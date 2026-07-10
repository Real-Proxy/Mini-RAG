import time
import json

from evaluation.dataset import evaluation_dataset
from src.query import ask_question
from datasets import Dataset

from ragas import EvaluationDataset, evaluate
from ragas.run_config import RunConfig

from ragas.metrics import (
    Faithfulness,
    ResponseRelevancy,
    LLMContextPrecisionWithoutReference,
    LLMContextRecall,
)

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from src.llm import llm
from src.embeddings import embeddings


def build_evaluation_dataset():

    evaluation_data = []

    total = len(evaluation_dataset)

    for i, sample in enumerate(evaluation_dataset, start=1):

        question = sample["question"]
        ground_truth = sample["ground_truth"]

        print("\n" + "=" * 80)
        print(f"Question {i}/{total}")
        print("=" * 80)
        print(question)

        result = ask_question(question)

        answer = result["answer"]
    
        contexts = result["contexts"]

        print("\nGenerated Answer")
        print("-" * 40)
        print(answer)

        print("\nGround Truth")
        print("-" * 40)
        print(ground_truth)

        #print("\nRetrieved Contexts")
        #print("-" * 40)

        #for j, context in enumerate(contexts, start=1):
            #print(f"\nContext {j}")
            #print(context)

        evaluation_data.append(
            {
            "user_input": question,
            "response": answer,
            "reference": ground_truth,
            "retrieved_contexts": contexts,
            }
        )

        if i < total:
            print("\nWaiting 5 seconds...")
            print("-" * 80)
            time.sleep(5)

    return evaluation_data


if __name__ == "__main__":

    evaluation_data = build_evaluation_dataset()

    print("\n" + "=" * 80)
    print("Evaluation Dataset Created Successfully")
    print("=" * 80)
    print(f"Total Questions: {len(evaluation_data)}")

    hf_dataset = Dataset.from_list(evaluation_data)
    ragas_dataset = EvaluationDataset.from_hf_dataset(hf_dataset)

    evaluator_llm = LangchainLLMWrapper(llm)
    evaluator_embeddings = LangchainEmbeddingsWrapper(embeddings)

    print("\nRunning RAGAS Evaluation...")
    print("=" * 80)

    run_config = RunConfig(
        timeout=240,
        max_retries=5,
        max_wait=120,
        max_workers=1,
        )   

    results = evaluate(
        dataset=ragas_dataset,
        metrics=[
            Faithfulness(),
            ResponseRelevancy(strictness=1),
            LLMContextPrecisionWithoutReference(),
            LLMContextRecall(),
        ],
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
        run_config=run_config,
    )

print("\n")
print("=" * 80)
print("RAGAS RESULTS")
print("=" * 80)

print(results)

df = results.to_pandas()

# Save detailed reports
df.to_csv(
    "evaluation/results/report.csv",
    index=False,
)

df.to_json(
    "evaluation/results/report.json",
    orient="records",
    indent=4,
)

# Create summary
summary = {
    "total_questions": len(df),
    "metrics": {
        "faithfulness": {
            "average": float(df["faithfulness"].mean()),
            "successful_evaluations": int(df["faithfulness"].count()),
            "null_values": int(df["faithfulness"].isnull().sum()),
        },
        "answer_relevancy": {
            "average": float(df["answer_relevancy"].mean()),
            "successful_evaluations": int(df["answer_relevancy"].count()),
            "null_values": int(df["answer_relevancy"].isnull().sum()),
        },
        "context_precision": {
            "average": float(df["llm_context_precision_without_reference"].mean()),
            "successful_evaluations": int(df["llm_context_precision_without_reference"].count()),
            "null_values": int(df["llm_context_precision_without_reference"].isnull().sum()),
        },
        "context_recall": {
            "average": float(df["context_recall"].mean()),
            "successful_evaluations": int(df["context_recall"].count()),
            "null_values": int(df["context_recall"].isnull().sum()),
        },
    },
}

with open("evaluation/results/summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("\n")
print("=" * 80)
print("SUMMARY")
print("=" * 80)

for metric, values in summary["metrics"].items():
    print(f"{metric:<20}: {values['average']:.4f}")

print("\nDetailed reports saved:")
print("  - evaluation/results/report.csv")
print("  - evaluation/results/report.json")
print("  - evaluation/results/summary.json")