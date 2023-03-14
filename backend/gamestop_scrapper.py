import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from server import ENV

url = "https://www.gamestop.com/video-games/nintendo-switch/products/metroid-prime-remastered---nintendo-switch/20003464.html?condition=Digital"
url2 = "https://www.gamestop.com/video-games/playstation-5/products/the-last-of-us-part-1----playstation-5/11206959-11206959.html?condition=Pre-Owned"
url3 = "https://www.gamestop.com/video-games/playstation-5/products/nba-2k23---playstation-5/11206859-11206849.html?condition=Pre-Owned"

def find_condition(url):
    """Find condition within URL"""
    condition_index = url.rfind('condition=')
    return url[condition_index+10:]

def fetch_price(url):
    if ENV == 'dev':
        chrome_options = Options()
        chrome_options.headless = True
        chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--allow-running-insecure-content')
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        # driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

    driver.get(url)

    price_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/span/span/span[1]'
    if len(driver.find_elements(By.XPATH, price_xpath)) > 0:
        price = driver.find_elements(By.XPATH, price_xpath)[0].text
    else:
        price = 0

    image_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/img'
    if len(driver.find_elements(By.XPATH, image_xpath)) > 0:
        image_src = driver.find_elements(By.XPATH, image_xpath)[0].get_attribute('src')
    else:
        image_src = 'https://media.istockphoto.com/id/1022028010/vector/image-unavailable-icon.jpg?s=612x612&w=0&k=20&c=7z3_vAq-RERxMXpVlouWRxswJINNlOgwkBZKlTCzMHg='

    condition = find_condition(url)
    print(condition)

    name_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/h2'
    if len(driver.find_elements(By.XPATH, name_xpath)) > 0:
        name = driver.find_elements(By.XPATH, name_xpath)[0].text
    else:
        name = ''
    
    driver.quit()
    return {'price': price, 'image_link': image_src, 'condition': condition, 'url': url, 'title': name}
