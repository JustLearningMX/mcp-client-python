from contextlib import AsyncExitStack
from typing import Optional

from anthropic import Anthropic
from mcp import ClientSession


class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.llm = Anthropic()
        self.tools = []
        self.messages = []
        # self.logger = logger

    # connect to the MCP server

    # call a mcp tool

    # get mcp tools list

    # process query

    # call llm

    # clean up

    ## extra

    # get conversation history