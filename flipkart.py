from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
import time
import sys

def get_flipkart_price(product_name):
    # Path to GeckoDriver
    service = Service(executable_path='/Users/shreyashivratriwar/Downloads/geckodriver')
    options = Options()
    options.binary_location = r'/Volumes/Firefox/Firefox.app'
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Open Flipkart
        driver.get("https://www.flipkart.com")

        # Close the login pop-up if it appears
        try:
            close_button = driver.find_element("css selector","button._2KpZ6l._2doB4z")
            close_button.click()
        except NoSuchElementException:
            pass  # No pop-up appeared

        # Find the search bar, enter the product name, and submit
        time.sleep(10)
        search_bar = driver.find_element("name","q")
        search_bar.send_keys(product_name)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the page to load
        time.sleep(10)

        # Find and print the price of the first product in search results
        try:
            price = driver.find_element('xpath','/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/div/a[3]/div/div[1]').text.replace('₹','').replace(',','')
        except:
            price = driver.find_element('css selector','._1_WHN1').text.replace('₹','').replace(',','')
        product_url = driver.current_url
        print(f"Price of '{product_name}': ₹{price}")

    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print("Error occurred.")
        print(e)
    finally:
        # Close the browser
        driver.quit()

# Example usage
try:
    get_flipkart_price(sys.argv[1])
except:
    get_flipkart_price(sys.argv)      