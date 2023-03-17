from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def fetch_price(url):
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

    driver.get(url)

    price_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div/div/span/span/span[1]'
    if len(driver.find_elements(By.XPATH, price_xpath)) > 0:
        price = driver.find_elements(By.XPATH, price_xpath)[0].text
    else:
        price = 0

    image_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/img'
    if len(driver.find_elements(By.XPATH, image_xpath)) > 0:
        image_src = driver.find_elements(By.XPATH, image_xpath)[0].get_attribute('src')
    else:
        image_src = 'https://media.istockphoto.com/id/1022028010/vector/image-unavailable-icon.jpg?s=612x612&w=0&k=20&c=7z3_vAq-RERxMXpVlouWRxswJINNlOgwkBZKlTCzMHg='

    condition_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[7]/div[3]/div/label/span[2]'
    if len(driver.find_elements(By.XPATH, condition_xpath)) > 0:
        condition = driver.find_elements(By.XPATH, condition_xpath)[0].text
    else:
        condition = ''

    name_xpath = '/html/body/div[6]/div[6]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/h2'
    if len(driver.find_elements(By.XPATH, name_xpath)) > 0:
        name = driver.find_elements(By.XPATH, name_xpath)[0].text
    else:
        name = ''
    
    driver.quit()
    return {'price': price, 'image_link': image_src, 'condition': condition, 'url': url, 'title': name}
