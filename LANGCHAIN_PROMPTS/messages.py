from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
#Human message is the message that human sends to the AI (input)
#AIMessage is the message that we get the output from the AI

messages = [
    SystemMessage(content='You ae a helpful assitant'),
    HumanMessage(content='Tell me about langChain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)