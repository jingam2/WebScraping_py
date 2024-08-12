from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# ChromeDriver의 경로를 설정합니다.
chrome_driver_path = r"C:\Users\82105\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # 다운로드한 chromedriver의 경로로 수정

# Chrome 옵션 설정 (headless 모드 비활성화)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 주석 처리하여 브라우저 창을 열도록 설정

# WebDriver 객체를 생성합니다.
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 뉴스 웹사이트 URL
url = "https://news.naver.com/breakingnews/section/101/258"
driver.get(url)

# 클릭할 최대 횟수를 설정합니다.
max_clicks = 5
click_count = 0

# 데이터를 저장할 리스트를 초기화합니다.
strong_texts = []

# 페이지가 로드될 때까지 대기
time.sleep(3)

while click_count < max_clicks:
    try:
        # '더보기' 버튼을 찾아 클릭합니다.
        more_button = driver.find_element(By.XPATH, '//*[@id="newsct"]/div[2]/div/div[2]/a')
        more_button.click()

        # 버튼 클릭 후 페이지 로드 대기
        time.sleep(2)

        click_count += 1
        print(f"Clicked 'More' button {click_count}/{max_clicks} times.")

    except Exception as e:
        print(f"Exception occurred: {e}")
        break

# 페이지의 모든 <strong> 태그를 찾습니다.
strong_tags = driver.find_elements(By.TAG_NAME, 'strong') # 다른 정보들도 태그활용하여 크롤링

for tag in strong_tags:
    text = tag.text.strip()
    if text:  # 텍스트가 비어 있지 않은 경우에만 추가합니다.
        strong_texts.append(text)

# WebDriver를 종료합니다.
driver.quit()

# 리스트를 데이터프레임으로 변환합니다.
df = pd.DataFrame(strong_texts, columns=['Strong Tag Text'])

# 데이터프레임 출력
print(df)

# 데이터프레임을 CSV 파일로 저장합니다.
df.to_csv('selenium_texts.csv', index=False)
