import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape infromation from LinkedIn profiles
    Manually scrape the information from the LinkedIn profile"""

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"  # 링크드인 API를 직접 사용하면 복잡하니까 proxycurl에서 제공하는 api를 사용
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()  # 필요한 데이터만 추출하자

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["People_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pip("profile_pic_url")

    return data
