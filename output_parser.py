from langchain.output_parsers import (
    PydanticOutputParser,
)  # 파이썬 내장 데이터 클래스와 매우 유사함 ( 실은 외부 라이브러리 ) , 스키마를 정의하고 스키마 입력의 유효성 검사 가능
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summmary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        description="Create ice breakers to open a conversation with the person"
    )

    def to_dict(
        self,
    ):  # 객체가 주어지면 해당 객체를 나타내는 딕셔너리 반환 -> 코드를 직렬화 할 때 사용. 딕셔너리로 전환하면 딕셔너리가 json으로 직렬화되어 서버가 응답
        return {
            "summary": self.summmary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
