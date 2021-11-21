"""
抓取hello-github的内容
https://hellogithub.com/periodical/category/Python%20%E9%A1%B9%E7%9B%AE/
"""
from utils.selenium_getter import get_headless_driver, get_normal_driver
from utils.dom_operator import DOMOperator as DO
from selenium.webdriver.common.by import By
import traceback

def scrape_python():
    url = "https://hellogithub.com/periodical/category/Python%20%E9%A1%B9%E7%9B%AE/"
    driver = get_normal_driver()
    xpath_names = {
        'title': '//*[@id="main"]/div[4]/h2[1]/a[2]',
        'content': '//*[@id="main"]/div[4]/p[1]'
    }
    driver.get(url)
    try:
        DO.add_names(driver, xpath_names)
        target_elements = DO.get_target_elements(driver,xpath_names)
        print(target_elements)
    except Exception as e:
        print(traceback.format_exc())
        driver.quit()

if __name__ == "__main__":
    scrape_python()