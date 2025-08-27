from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool

@CrewBase
class HotdealAgent:

    @agent
    def hotdeal_harvesting_agent(self):
        return Agent(
            config=self.agents_config["hotdeal_harvesting_agent"],
            tools=[search_tool, scrape_tool]
        )

    @task
    def hotdeal_harvesting_task(self):
        return Task(
            config=self.tasks_config["hotdeal_harvesting_task"],
        )

    @crew
    def crew(self):
        return Crew(
            tasks=self.tasks,
            agents=self.agents,
            verbose=True,
        )