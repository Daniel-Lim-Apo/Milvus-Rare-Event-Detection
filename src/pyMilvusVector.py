from pymilvus import MilvusClient
import numpy as np

client = MilvusClient("./milvus_kids.db")
# client.create_collection(
#     collection_name="kids_collection",
#     dimension=384  # The vectors we will use in this demo has 384 dimensions
# )

if client.has_collection(collection_name="kids_collection"):
    client.drop_collection(collection_name="kids_collection")
client.create_collection(
    collection_name="kids_collection",
    dimension=768,  # The vectors we will use in this demo has 768 dimensions
)

# Text strings to search from.
# docs = [
#     "Artificial intelligence was founded as an academic discipline in 1956.",
#     "Alan Turing was the first person to conduct substantial research in AI.",
#     "Born in Maida Vale, London, Turing was raised in southern England.",
# ]

from pymilvus import model

# If connection to https://huggingface.co/ failed, uncomment the following path
# import os
# os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# This will download a small embedding model "paraphrase-albert-small-v2" (~50MB).
embedding_fn = model.DefaultEmbeddingFunction()
print('Lendo o arquivo...\n')
file_path = 'kids_activities_50.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

docs = lines

# For illustration, here we use fake vectors with random numbers (384 dimension).

# vectors = [[ np.random.uniform(-1, 1) for _ in range(384) ] for _ in range(len(docs)) ]
# data = [ {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"} for i in range(len(vectors)) ]
# res = client.insert(
#     collection_name="kids_collection",
#     data=data
# )

vectors = embedding_fn.encode_documents(docs)

# The output vector has 768 dimensions, matching the collection that we just created.
print("Dim:", embedding_fn.dim, vectors[0].shape)  # Dim: 768 (768,)

# Each entity has id, vector representation, raw text, and a subject label that we use
# to demo metadata filtering later.
data = [
    {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
    for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))

res = client.insert(collection_name="kids_collection", data=data)
print(res)


# # This will exclude any text in "history" subject despite close to the query vector.
# res = client.search(
#     collection_name="kids_collection",
#     data=[vectors[0]],
#     filter="subject == 'history'",
#     limit=2,
#     output_fields=["text", "subject"],
# )
# print(res)

# # a query that retrieves all entities matching filter expressions.
# res = client.query(
#     collection_name="kids_collection",
#     filter="subject == 'history'",
#     output_fields=["text", "subject"],
# )
# print(res)

# # delete
# res = client.delete(
#     collection_name="kids_collection",
#     filter="subject == 'history'",
# )
# print(res)