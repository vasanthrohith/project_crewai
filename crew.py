from crewai import Crew,Process
from tasks import research_task, write_task
from myagents import news_researcher, news_writter

crew = Crew(
    agents=[news_researcher,news_writter],
    tasks=[research_task,write_task],
    process=Process.sequential
)
def start_crew(text):
    result = crew.kickoff({"topic":text})
    print(result)
    return result