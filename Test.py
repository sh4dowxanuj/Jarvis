import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True

# Use os.path.join for platform-independent path
path = os.path.join("DataBase1", "chromedriver.exe")
driver = webdriver.Chrome(path, options=chrome_options)
driver.maximize_window()

website = "https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)

# Wait until the dropdown is present and select 'British English / Brian'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sprachwahl"))
)
button_selection = Select(driver.find_element(By.ID, "sprachwahl"))
button_selection.select_by_visible_text('British English / Brian')

def speak(text):
    if text:
        print(f"\nJARVIS: {text}\n")
        data = str(text)

        # Wait until the textarea is present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "voicetext"))
        )
        textarea = driver.find_element(By.ID, "voicetext")
        textarea.clear()
        textarea.send_keys(data)

        # Wait until the 'Read Aloud' button is clickable and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "vorlesenbutton"))
        )
        driver.find_element(By.ID, "vorlesenbutton").click()

        # Determine sleep duration based on text length
        length_of_text = len(data)
        if length_of_text >= 100:
            sleep(14)
        elif length_of_text >= 70:
            sleep(10)
        elif length_of_text >= 55:
            sleep(8)
        elif length_of_text >= 40:
            sleep(6)
        elif length_of_text >= 30:
            sleep(4)
        else:
            sleep(2)

# Example usage
speak("Hello, this is a test message.")
