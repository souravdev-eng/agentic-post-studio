from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI

MODEL_NAME = "gpt-4o-mini"
OPENAI_LLM = ChatOpenAI(model=MODEL_NAME, temperature=0)
