from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedIn_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parser import person_intel_parser

from dotenv import load_dotenv
import os


def ice_break(name: str) -> str:

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco Udemy")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them 
        3. A topic that may interest them
        4. 2 creative Ice breakers to open a conversation with them.
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information"],
        template=summary_template,
        partial_variables= {
            "format_instructions": person_intel_parser.get_format_instructions()
        }
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(information=linkedin_data)

    return result


if __name__ == "__main__":
    print("Hello Langchain!")

    ice_break(
        name="Harrison Chase"
    )  # 아웃풋 파서를 통해 프론트엔드에서 간편하게 쓸 수 있는 파이썬 객체를 돌려받자 -> 어플리케이션 개발에 유리함.
