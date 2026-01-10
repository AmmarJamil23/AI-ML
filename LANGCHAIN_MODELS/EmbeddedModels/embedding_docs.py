from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Islamabad is the capital of Pakistan",
    "Beijing is the capital of  China",
]

res = embedding.embed_documents(documents)

print(str(res))

