### End to end Agentic AI chatbots demo

## Main components:

# Basic chatbot graph

        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class
        and integrates it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.

# Chatbot with web search tool integration

        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.

# AI news summarizer

        Adds more complexity to the agentic pipeline by improving the summary
        of results returmed from the chatbot tool. This summarizer also
        includes options for daily, weekly and monthly news.
