# MCP Basic Agent

This sample shows how to integrate an ADK agent with a Model Context Protocol (MCP) tool.
It launches the MCP filesystem server via `npx` and allows the agent to read files
within this directory.

## Running

1. Ensure you have Node and `npx` installed.
2. Start the ADK Web UI using this agent:

   ```bash
   adk web --agent-path contributing/samples/mcp_basic_agent
   ```

The agent will automatically start the MCP server and expose read-only file
operations such as `read_file` and `list_directory`.
