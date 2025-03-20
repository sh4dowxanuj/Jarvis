   
#Chrome Based
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True

# Use os.path.join for platform-independent path
Path = os.path.join("DataBase1", "chromedriver.exe")
driver = webdriver.Chrome(Path, options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(By.XPATH, value='//select[@id="sprachwahl"]'))
ButtonSelection.select_by_visible_text('British English / Brian')

def Speak(Text):
    lengthoftext = len(str(Text))
    
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"JARVIS : {Text}.")
        print("")
        Data = str(Text)
        
        # Corrected XPath for the textarea
        xpathofsec = '//textarea[@id="voicetext"]'
        driver.find_element(By.XPATH, value=xpathofsec).send_keys(Data)
        
        # Corrected XPath for the play button
        driver.find_element(By.XPATH, value='//input[@id="vorlesenbutton"]').click()
        
        # Clear the textarea after playing
        driver.find_element(By.XPATH, value='//textarea[@id="voicetext"]').clear()
        
        if lengthoftext >= 100:
            sleep(14)
        elif lengthoftext >= 70:
            sleep(10)
        elif lengthoftext >= 55:
            sleep(8)
        elif lengthoftext >= 40:
            sleep(6)
        elif lengthoftext >= 30:
            sleep(4)
        else:
            sleep(2)
