from pymilvus import MilvusClient
from pymilvus import model
import numpy as np

embedding_fn = model.DefaultEmbeddingFunction()

client = MilvusClient("./milvus_kids.db")
# This will exclude any text in "history" subject despite close to the query vector.

res = client.search(
    collection_name="kids_collection",
    data=embedding_fn.encode_queries(["P1 is playing basket"]),
    # filter="subject == 'biology'",
    limit=5,
    output_fields=["text", "subject"],
)

print(res)