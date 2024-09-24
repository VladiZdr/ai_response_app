from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--headless")

# Set up Chrome WebDriver service with the path to your chromedriver
service = Service("D:/chrome_driver/chromedriver.exe")  # Replace with the actual path to your chromedriver

# Initialize the WebDriver in headless mode
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the website
driver.get("https://deepai.org/chat")
time.sleep(2)

chatbox = driver.find_element(By.CLASS_NAME, "chatbox")

def chat_with_ai(user_input_in_chat):
    response_text = ""
    try:
        # Find the text area by its class and enter the user input
        chatbox.send_keys(user_input_in_chat)  # Input from your app
        #finish input
        chatbox.send_keys(Keys.RETURN)

        # Wait for response
        time.sleep(5)

        # Find the response container by its class and extract the text
        response_container = driver.find_element(By.CLASS_NAME, "markdownContainer")
        response_text = response_container.text


    finally:
        return response_text

# Close the browser window
def close_link():
        driver.quit()

# Example usage
user_input = "What is artificial intelligence?"
response = chat_with_ai(user_input)
print("AI Response:", response)
close_link()