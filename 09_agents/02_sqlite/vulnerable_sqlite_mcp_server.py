from fastmcp import FastMCP
import sqlite3
import sys

mcp = FastMCP("sqlite")

@mcp.tool()
def query(query: str) -> str:
    """Query a Sqlite3 database. Returns the result of the query."""
    database = "./db_data/metactf_users.db"
    con = sqlite3.connect(database)
    cur = con.cursor()
    results = cur.execute(query)
    con.commit()
    output_string = '\n'.join([', '.join(map(str, row)) for row in results])
    return output_string

if __name__ == "__main__":
    if sys.argv[1] == 'stdio':
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host="0.0.0.0", port=8080)
