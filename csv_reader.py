from langchain.agents import AgentExecutor , create_react_agent
from langchain_openai import  ChatOpenAI
from langchain_experimental .agents.agent_toolkits import create_csv_agent
from langchain_core . tools import Tool
from langchain import hub
from langchain_experimental.tools import PythonREPLTool
import os
from typing import Any
from langchain_core.tools import tool
def csv_reader(original_prompt: str) -> str:
    csv_agent_executor: AgentExecutor = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-4"),
        path="episode_info.csv",
        verbose=True,
        allow_dangerous_code=True
    )

    print(f"the original prompt that has been passed is {original_prompt}")

    # Run query
    result = csv_agent_executor.invoke({"input": original_prompt})

    # Return just the final answer
    return result["output"]
