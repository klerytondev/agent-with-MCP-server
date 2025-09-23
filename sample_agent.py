from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from tools import get_company_info, get_history_stock_price, get_current_stock_price

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

memory = MemorySaver()
systen_message = "You are a helpful assistant that helps people find information."

tools = [get_company_info, 
         get_history_stock_price, 
         get_current_stock_price]

agent_executor = create_react_agent(
    llm=llm,
    tools=tools,
    system_message=systen_message,
    memory_saver=memory,
    verbose=True,
)

config = {'configurable': {'threads': '1'}}

while True:
    imput_message = {
        'role': 'user',
        'content': input("Enter your question: "),
    }
    for step in agent_executor.stream(
        {'messages': [imput_message]}, config, stream_mode='value'
    ):
        step['messages'][-1].pretty_print()
    
