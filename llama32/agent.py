from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# initiage model
my_local_assistant = LiteLlm(model="ollama_chat/llama3.2")

# create root agent

root_agent = Agent(
    name="my_local_assistant",
    model=my_local_assistant,
    description="Local running llama 3.2 model",
    instruction="You are an assistant that help assist provide financial assistance only. Do not assist query from any other domain or area.",
    tools=[]
)
