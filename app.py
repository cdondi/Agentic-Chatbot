import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.langgraph_agentic_ai.main import load_langgraph_agenticai_app

if __name__ == "__main__":
    load_langgraph_agenticai_app()
