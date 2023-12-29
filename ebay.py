from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys

def get_ebay_price(product_name):
    service = Service(executable_path='/Users/shreyashivratriwar/Downloads/geckodriver')
    options = Options()
    options.binary_location = r'/Volumes/Firefox/Firefox.app'
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("https://www.ebay.com")

        search_bar = driver.find_element('id','gh-ac')  # eBay's search bar ID
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

        time.sleep(5)  # Wait for the page to load

        # Find the price of the first listed product
        # The selector might need to be updated based on eBay's layout
        price = driver.find_element('xpath','/html/body/div[4]/div[4]/div[2]/div[1]/div[2]/ul/li[2]/div/div[2]/div[3]/div[1]/span').text
        product_url = driver.current_url
        print(f"Price of '{product_name}': {price}")

    except NoSuchElementException as e:
        return "Price not found. Error: " + str(e)
    finally:
        driver.quit()

# Example usage
try:
    get_ebay_price(sys.argv[1])
except:
    get_ebay_price(sys.argv)