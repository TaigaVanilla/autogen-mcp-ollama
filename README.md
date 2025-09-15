# AI Agent with Ollama and MCP Server

This repository contains an AI agent that uses Ollama to run local LLMs as the model backend and communicates with an MCP (Model Context Protocol) server running inside Docker. The agent demonstrates file system operations through the MCP server.

## What This Agent Does

The agent is designed to:
- Use a local LLM (via Ollama) for natural language processing
- Connect to an MCP server running in Docker for file system operations
- Demonstrate file creation and manipulation capabilities
- Show how to integrate AutoGen agents with MCP servers

## Prerequisites

Before running this agent, ensure you have the following installed:

1. **Python 3.8+** - The agent is built with Python
2. **Ollama** - For running local LLMs
   - Install from [https://ollama.ai](https://ollama.ai)
   - Pull the required model: `ollama pull qwen3:4b`
3. **Docker** - For running the MCP server
   - Install from [https://docker.com](https://docker.com)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd autogen-mcp-ollama
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Pull the required Ollama model:
   ```bash
   ollama pull qwen3:4b
   ```

4. Start Ollama service:
   ```bash
   ollama serve
   ```
   (Keep this running in a separate terminal)

## Running the Agent

1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Run the agent:
   ```bash
   python3 filesystem_agent.py
   ```

## Example Usage

When you run the agent, it will automatically:

1. Initialize the Ollama client with the `qwen3:4b` model
2. Start the MCP server in Docker with the workspace mounted
3. Create a test file at `/projects/workspace/test.txt`
4. Display the operation result

The agent uses the following configuration:
- Model: `qwen3:4b` (supports function calling)
- Ollama URL: `http://localhost:11434/v1`
- Workspace: `/Users/user-name/Downloads/autogen-mcp-ollama/workspace` (mounted to `/projects/workspace` in Docker)
