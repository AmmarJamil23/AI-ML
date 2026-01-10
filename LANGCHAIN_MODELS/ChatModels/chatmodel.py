from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# tempperature is parameter that is used to control determinism of the output text

model = ChatOpenAI(model='gpt-4', temperature=1.5)

result = model.invoke("Write lyrics of sing about me i am dying of thirst by kendrick lamar ")

print(result.content)