from fastmcp import FastMCP
import os

mcp = FastMCP("GoalMisgenExplorer")

#search area
Base_dir = os.path.dirname(os.path.abspath(__file__))

@mcp.tool()
def search_file(world: str, filename: str) -> str:
    """
    Searches a specific world (train or test) for a file.
    Args:
        world: Environment name
        filename: File to look for
    """
    path = os.path.join(Base_dir, "data", world, filename)
    try:
        with open(path, "r") as f:
            content = f.read()
            return f"FOUND in {filename}: {content}"
    except FileNotFoundError:
        return f"Error: {filename} not found in {world}"
if __name__ == "__main__":
    mcp.run()