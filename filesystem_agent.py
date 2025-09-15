import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_core.models import ModelInfo
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools


model_client = OllamaChatCompletionClient(
    model="qwen3:4b",  # You can modify the model to use a different model
    base_url="http://localhost:11434/v1",
    model_info=ModelInfo(
        vision=False, function_calling=True, json_output=False, family="unknown"
    ),
)


async def main() -> None:
    server_params = StdioServerParams(
        command="docker",
        args=[
            "run",
            "-i",
            "--rm",
            "--mount",
            "type=bind,src=/Users/user-name/Downloads/autogen-mcp-ollama/workspace,dst=/projects/workspace",  # You can modify the workspace path
            "mcp/filesystem",
            "/projects",
        ],
    )

    tools = await mcp_server_tools(server_params)

    agent = AssistantAgent(
        name="filesystem_operator",
        model_client=model_client,
        tools=tools,
        model_client_stream=False,
        reflect_on_tool_use=True,
        max_tool_iterations=3,
    )

    print(
        await agent.run(
            task="Create a file called /projects/workspace/test.txt with some content",  # You can modify the task
            cancellation_token=CancellationToken(),
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
