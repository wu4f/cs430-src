import os
from langchain_google_genai import ChatGoogleGenerativeAI, HarmCategory, HarmBlockThreshold
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_core.output_parsers import StrOutputParser
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio
llm = ChatGoogleGenerativeAI(
             model=os.getenv("GOOGLE_MODEL"),
             safety_settings = {
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
             }
      )
#from langchain_openai import ChatOpenAI
#llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"))
#from langchain_anthropic import ChatAnthropic
#llm = ChatAnthropic(model=os.getenv("ANTHROPIC_MODEL"))

prompt = f"You are a Sqlite3 database look up tool. Perform queries on a database hosted by the specified MCP server given the user's input.  Utilize the user input verbatim when sending the query to the database and print the query that was sent to the database"

async def run_agent():
    async with streamablehttp_client(f"{os.getenv('MCP_URL')}/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            agent = create_agent(model=llm, tools=tools, system_prompt=prompt)
            history = []

            print(f"Welcome to my database querying agent.  The agent will query the SQLite MCP server to answer queries.")

            while True:
                line = input("llm>> ")
                if line:
                    try:
                        history.append(HumanMessage(content=line))
                        result = await agent.ainvoke({"messages": history})
                        # Extract the actual message content from the agent's response
                        if "messages" in result and result["messages"]:
                            response_content =  StrOutputParser().invoke(result["messages"][-1])
                            history.append(AIMessage(content=response_content))
                            print(response_content)
                        else:
                            print("No response from agent")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    break

if __name__ == "__main__":
    asyncio.run(run_agent())
