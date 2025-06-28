# google-adk-ollama

This example will help set up your local windows system to set up -
google-adk, Ollama supported LLM models

In this example you will understand how to run multi agent system on our local machine.

Step 1 - create virtual env
python -m venv .venv

Step 2 - install UV
pip install uv

Step 3 - INstall google-adk
uv pip install google-adk

Step 4 - Install LiteLlm
uv pip install litellm

Step 5 - environment variable for local ollama model that's running your machine
set OLLAMA_API_BASE = "http://localhost:11434"

for the purpose of this example I have set up root agent with no tool features and only llama3.2 interactive capability

root_agent = Agent(
name="my_local_assistant",
model=my_local_assistant,
description="Local running llama 3.2 model",
instruction="You are an assistant that help assist provide financial assistance only. Do not assist query from any other domain or area.",
tools=[]
)

Step 6 - run adk (adk web for interactive session) 
type : adk web

Once everything works, your output should similar like this -
![image](https://github.com/user-attachments/assets/aa144b2b-756e-47d9-a00d-b97b3fc78a97)

