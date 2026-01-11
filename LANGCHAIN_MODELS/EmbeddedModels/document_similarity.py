from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
     "Machine learning is a field of computer science that focuses on building systems that can learn from data and improve over time without being explicitly programmed.",

    "Artificial intelligence refers to the broader concept of creating machines that are capable of performing tasks which normally require human intelligence.",

    "Python programming is widely used in data science and artificial intelligence because it is simple to read, easy to write, and supported by a large ecosystem of libraries.",

    "Language models are a type of artificial intelligence designed to understand and generate human language by learning patterns from large amounts of text.",

    "Modern artificial intelligence systems rely on large datasets and powerful computation to analyze information, recognize patterns, and make meaningful predictions."
]

query = "tell me about python programming"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
print(list(enumerate(scores)))