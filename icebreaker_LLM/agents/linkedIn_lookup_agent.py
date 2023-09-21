"""
Agent는 LLM을 이용하여 어떤 Action*이 어느 단계에서 이루어져야하는지 판단하여 task를 수행한다.

* action이란 간단하게는 output을 유저에게 리턴하는 것부터 tool*을 사용하는 등의 행위를 모두 의미한다.
* tool: 특정한 임무를 수행하는 function. Google Search, DB Lookup, Python REPL 등이 해당될 수 있다.
"""

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


from dotenv import load_dotenv
import os


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to theri LikedIn profile page.
                            Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the LinkedIn Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )  # 에이전트 유형은 저마다 고유한 작동을함

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linked_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linked_profile_url
