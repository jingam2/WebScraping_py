from bs4 import BeautifulSoup
import requests
import pandas as pd

# 뉴스 웹사이트 URL
url = "https://news.naver.com/breakingnews/section/101/258"

# HTTP GET 요청을 보냅니다.
response = requests.get(url)

# HTTP 응답이 성공적이면 HTML 문서를 파싱합니다.
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 모든 <strong> 태그를 찾습니다.
    strong_tags = soup.find_all('strong')

    # <strong> 태그의 텍스트를 저장할 리스트를 초기화합니다.
    strong_texts = []

    for tag in strong_tags:
        text = tag.get_text(strip=True)
        strong_texts.append(text)  # 리스트에 텍스트를 추가합니다.

    # 리스트를 데이터프레임으로 변환합니다.
    df = pd.DataFrame(strong_texts, columns=['기사제목'])

    # 데이터프레임 출력
    print(df)

    # 데이터프레임을 CSV 파일로 저장합니다.
    df.to_csv('bs_texts.csv', index=False)
else:
    print("Failed to retrieve the page")
