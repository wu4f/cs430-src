import os
import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI, HarmCategory, HarmBlockThreshold
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_MODEL"),
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))
# from langchain_anthropic import ChatAnthropic
# llm = ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"))
import logging
logging.getLogger("langchain_google_genai").setLevel(logging.ERROR)

prompt = (
    "You are a Sqlite3 database look up tool. Perform queries on a database hosted by "
    "the specified MCP server given the user's input.  Utilize the user input verbatim "
    "when sending the query to the database and print the query that was sent to the database"
)


async def run_agent():
    # The transport is inferred from the URL; no ClientSession / initialize() needed.
    async with MCPAdapter(f"{os.getenv('MCP_URL')}/mcp") as adapter:
        tools = await adapter.list_tools()

        agent = create_agent(model=llm, tools=tools, system_prompt=prompt)
        history = []

        print("Welcome to my database querying agent.  The agent will query the SQLite MCP server to answer queries.")

        while True:
            line = input("llm>> ")
            if not line:
                break
            try:
                result = await agent.ainvoke({"messages": [("user", line)]})
                for msg in result.get("messages", []):
                    if isinstance(msg, AIMessage):
                        for call in msg.tool_calls:
                            print(f"[request] {call['name']}({call['args']})")
                    elif isinstance(msg, ToolMessage):
                        print(f"[response] {msg.text}")
                messages = result.get("messages")
                print(messages[-1].text if messages else "No response from agent")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_agent())
