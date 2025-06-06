import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

_allowed_path = os.path.dirname(os.path.abspath(__file__))

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="mcp_filesystem_agent",
    instruction=f"""
Use the provided MCP tools to read files under {_allowed_path}.
Only read operations are allowed.
""",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-filesystem", _allowed_path],
                ),
                timeout=5,
            ),
            tool_filter=[
                "read_file",
                "read_multiple_files",
                "list_directory",
                "directory_tree",
                "search_files",
                "get_file_info",
                "list_allowed_directories",
            ],
        )
    ],
)
