from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys

def get_amazon_price(product_name):
    # Path to GeckoDriver
    service = Service(executable_path='/Users/shreyashivratriwar/Downloads/geckodriver')
    options = Options()
    options.binary_location = r'/Volumes/Firefox/Firefox.app'
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)


    try:
        # Open Amazon.in
        driver.get("https://www.amazon.in")
        time.sleep(2)
        # Find the search bar, enter the product name, and submit
        search_bar = driver.find_element('id','twotabsearchtextbox')
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the page to load()
        time.sleep(2)

        # Find and print the price of the first product in search results
        price = driver.find_element('css selector','.a-price-whole').text.replace('₹','').replace(',','')
        print(f"Price of '{product_name}': ₹{price}")

    except NoSuchElementException as e:
        print("Error: Element not found.")
        print(e)
    finally:
        # Close the browser
        driver.quit()

# Example usage
try:
    get_amazon_price(sys.argv[1])
except:
    get_amazon_price(sys.argv)    