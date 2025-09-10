from fastmcp import FastMCP
import sqlite3
import sys

mcp = FastMCP("sqlite")

@mcp.tool()
def query(query: str, path: str) -> str:
    """Query a specified Sqlite3 database. Returns the result of the query."""
    con = sqlite3.connect(path)
    cur = con.cursor()
    res = cur.execute(query)
    con.commit()
    return res.fetchall()

if __name__ == "__main__":
    if sys.argv[1] == 'stdio':
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host="0.0.0.0", port=8080)
