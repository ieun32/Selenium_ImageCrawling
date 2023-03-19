import time 
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#이미지 크롤링 하고 싶은 단어 입력
keyword = '팬케이크'

#브라우저 자동 닫힘 방지
options = Options()
options.add_experimental_option('detach', True) 

#웹드라이버 불러오기
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#브라우저 열기, 이미지 검색창으로 이동
driver.get('https://google.co.kr/imghp')
driver.implicitly_wait(time_to_wait=10)

#검색창에 키워드 검색
keyElement = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')   #cursor
keyElement.send_keys(keyword)                                                                                       #input
keyElement.send_keys(Keys.RETURN)                                                                                   #Enter

#스크롤
bodyElement = driver.find_element(By.TAG_NAME, 'body')
time.sleep(2)

for i in range(10):
    bodyElement.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

#고화질 원본 이미지 다운
images = driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div/a[1]')

imageSeq = 1
for image in images:
    image.click()
    time.sleep(0.5)
    highImages = driver.find_elements(By.CSS_SELECTOR, '#Sva75c > div.DyeYj > div > div.dFMRD > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id.b0vFpe > div > a > img')
    realImage = highImages[0].get_attribute('src')

    try:
        urllib.request.urlretrieve(realImage, 'C:/GoogleImage_Pancake/' + str(imageSeq) + '.jpg')
        imageSeq += 1
    except:
        pass
