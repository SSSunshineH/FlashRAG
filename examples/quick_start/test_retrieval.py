from flashrag.config import Config
from flashrag.retriever import DenseRetriever


config_dict = {
    "data_dir": "dataset/",
    "index_path": "indexes/e5_Flat.index",
    "corpus_path": "indexes/general_knowledge.jsonl",
    "model2path": {
        "e5": "/Users/sunshineh/Downloads/FlashRAG/models/e5-base-v2"
    },
    "retrieval_method": "e5",
    "retrieval_topk": 3,
}

config = Config(config_dict=config_dict)

retriever = DenseRetriever(config)

query = "Who was the first person to walk on the Moon?"

result = retriever.search(query)

print("\n=== QUERY ===")
print(query)

print("\n=== RETRIEVED DOCUMENTS ===")
for i, doc in enumerate(result):
    print(f"\n--- Document {i + 1} ---")
    print(doc)