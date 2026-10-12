from mcp.server.mcpserver import MCPServer

mcp: MCPServer = MCPServer("MyMathServer")


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b


@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtracts b from a."""
    return a - b


if __name__ == "__main__":
    print("🚀 Starting My Math Server on http://127.0.0.1:54321/sse ...")
    mcp.run(transport="sse", host="127.0.0.1", port=54321)