from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys

def get_gem_price(product_name):
    # Path to GeckoDriver
    service = Service(executable_path='/Users/shreyashivratriwar/Downloads/geckodriver')
    options = Options()
    options.binary_location = r'/Volumes/Firefox/Firefox.app'
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Open GeM website
        driver.get("https://gem.gov.in")
        

        driver.set_window_size(1024, 600)
        driver.maximize_window()

        while True:
                try:
                    time.sleep(2)
                    search_bar = driver.find_element('css selector','input.form-control:nth-child(2)')
                    search_bar.click()
                    search_bar.send_keys(product_name)
                    search_bar_click = driver.find_element('css selector', 'div.input-field:nth-child(3) > button:nth-child(1) > i:nth-child(1)')
                    search_bar_click.click()
                    break # leave while loop
                except TimeoutException:
                    driver.refresh()

        # TODO: Add steps for handling login, if necessary

        # Find the search bar, enter the product name, and submit
        # Note: The exact method to find the search bar will depend on the website's layout
        

        # Wait for the page to load
        time.sleep(2)
        driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div/div/div/ul/li[1]/ul/li[1]/a').click()
        time.sleep(2)
        # Extract the relevant information
        # Note: The method to find the price or other details will depend on how the website displays them
        price = driver.find_element(By.CLASS_NAME,'variant-final-price').text.replace('₹','').replace(',','')  # Replace with actual selector
        product_url = driver.current_url
        print(f"Price of '{product_name}': ₹{price}")

    except NoSuchElementException as e:
        print("Error occurred.")
        print(e)
    finally:
        # Close the browser
        driver.quit()

try:
    get_gem_price(sys.argv[1])
except:
    get_gem_price(sys.argv)   