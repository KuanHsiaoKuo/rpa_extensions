from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/)
#download_url = 'https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_mac64.zip'
#download_url = 'https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_mac64.zip'
download_url = 'https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_mac64.zip'

def get_headless_driver():
    chrome_options = Options()
    chromedriver_path = "./chromedriver"
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--headless")  # 使用无头谷歌浏览器模式
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = (
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
    # 指定谷歌浏览器路径
    try:
        driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
    except Exception as e:
        os.system(
            f"wget {download_url}"
        )
        os.system("unzip chrome*.zip")
        os.system("rm chrome*.zip")
        driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
    return driver


def get_normal_driver():
    chromedriver_path = "./chromedriver"
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--disable-gpu")
    try:
        driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)
    except Exception as e:
        import pdb;pdb.set_trace()
        os.system(
            f"wget {download_url}"
        )
        os.system("unzip chrome*.zip")
        os.system("rm chrome*.zip")
        driver = webdriver.Chrome(executable_path=chromedriver_path)
    return driver


if __name__ == "__main__":
    chromedriver_path = "ChromeDriver"
    driver = get_normal_driver()
    # driver = get_headless_driver()
    driver.get("http://www.baidu.com")
