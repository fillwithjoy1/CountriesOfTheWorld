from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# List of all countries in the world
countries = [
    'Afghanistan', 'Albania', 'Algeria', ...
    # Add all the countries here
]

# Initialize the web driver
driver = webdriver.Edge()

# Navigate to the quiz website
driver.get('https://www.sporcle.com/games/g/world')

# Identify and click the button element
button_element = driver.find_element(by=By.ID, value='button_play')
button_element.click()


# Wait for Edge to finish loading the webpage
def web_page_loaded(driver):
    return driver.execute_script("return initialized")


WebDriverWait(driver, timeout=10).until(web_page_loaded)

# Identify the input element on the quiz web page
input_element = driver.find_element(by=By.ID, value='gameinput')

# Iterate through the list of countries and enter each one into the input element
for country in countries:
    input_element.clear()
    input_element.send_keys(country)
    input_element.send_keys(Keys.RETURN)
    time.sleep(1)  # Add a delay to avoid being blocked or flagged as a bot

# Close the browser
# driver.quit()
