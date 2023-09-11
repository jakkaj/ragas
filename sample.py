from ragas import evaluate
from datasets import Dataset
import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv(".env", verbose=True)


# prepare your huggingface dataset in the format
# Dataset({
#     features: ['question', 'contexts', 'answer'],
#     num_rows: 25
# })

dataset: Dataset

results = evaluate(dataset)
# {'ragas_score': 0.860, 'context_relevancy': 0.817,
# 'faithfulness': 0.892, 'answer_relevancy': 0.874}