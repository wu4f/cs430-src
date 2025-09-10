import os
import sys
import readline
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
import asyncio
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model=os.getenv("GOOGLE_MODEL"))
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))
#from langchain_anthropic import ChatAnthropic
#llm = ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"))

try: 
    database = sys.argv[1]
except:
    # No database specified
    database = "db_data/metactf_users.db"

server = StdioServerParameters(
    command="python",
    args=["vulnerable_sqlite_mcp_server_stdio.py","stdio"]
)

prompt = f"You are a Sqlite3 database look up tool. Perform queries on the database at {database} given the user's input.  Utilize the user input verbatim when sending the query to the database and print the query that was sent to the database"

async def run_agent():
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_react_agent(model=llm, tools=tools, prompt=prompt)

            print(f"Welcome to my database querying agent.  The agent will query the SQLite MCP server to answer queries on the database at {database}.")

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
