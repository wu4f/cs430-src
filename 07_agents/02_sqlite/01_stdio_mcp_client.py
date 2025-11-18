import os
import readline
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model=os.getenv("GOOGLE_MODEL"))
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))
#from langchain_anthropic import ChatAnthropic
#llm = ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"))

server = StdioServerParameters(
    command="python",
    args=["vulnerable_sqlite_mcp_server.py","stdio"]
)

prompt = f"You are a Sqlite3 database look up tool. Perform queries on a database hosted by the specified MCP server given the user's input.  Utilize the user input verbatim when sending the query to the database and print the query that was sent to the database"

async def run_agent():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_agent(model=llm, tools=tools, system_prompt=prompt, debug=True)

            print(f"Welcome to my database querying agent.  The agent will query the SQLite MCP server to answer queries.")

            while True:
                line = input("llm>> ")
                if line:
                    try:
                        result = await agent.ainvoke({"messages": [("user", line)]})
                        # Extract the actual message content from the agent's response
                        if "messages" in result:
                            messages = result["messages"]
                            if messages:
                                last_message = messages[-1]
                                if hasattr(last_message, 'content'):
                                    print(f"{last_message.content}")
                                else:
                                    print(f"{last_message}")
                            else:
                                print("No response from agent")
                        else:
                            print(f"Agent response: {result}")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    break

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)
