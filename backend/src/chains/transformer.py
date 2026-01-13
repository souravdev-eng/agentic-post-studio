from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.config.model_config import OPENAI_LLM

SYSTEM_PROMPT = """
You are an expert content writer in LinkedIn. Your job is to understand the user's query and transform the query for more clarity.
After that add all the relevant details to the query for better engaging content. Your goal is  to just transform the query and return only
the transformed query. Where we will pass the transformed query to an LLM to generate the post.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("user", "Transform the following query for better engaging content: {query}"),
    ]
)

transformer_chain = prompt | OPENAI_LLM | StrOutputParser()
