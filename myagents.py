from langchain_community.llms import HuggingFaceEndpoint
from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_tool

load_dotenv()

huggingfacehub_api_key= os.getenv("HUGGINGFACEHUB_API_TOKEN")
serper_api_key=os.getenv("SERPER_API_KEY")
google_api_key=os.getenv("GOOGLE_API_KEY")



## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=google_api_key)
# print(llm.invoke("Hi"))

news_researcher = Agent(
    role = "Senior researcher",
    goal = "uncover groudbreaking technology in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools = [search_tool],
    llm=llm,
    allow_delegation=True
)

news_writter = Agent(
    role = "Senior researcher",
    goal = "Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [search_tool],
    llm=llm,
    allow_delegation=False
)
