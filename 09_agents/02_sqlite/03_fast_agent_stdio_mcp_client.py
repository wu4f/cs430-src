import asyncio
import sys
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("SQLite Agent")

try:
    database = sys.argv[1]
except:
    # No database specified
    database = "db_data/metactf_users.db"


@fast.agent(
    instruction=f"You are a Sqlite3 database look up tool. Perform queries on the database at {database} given the user's input.  Utilize the user input verbatim when sending the query to the database and print the query that was sent to the database",
    model="gpt-4.1",
    servers=["sqlite"],
    use_history=True,
)
async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
