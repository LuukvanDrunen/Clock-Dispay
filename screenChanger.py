#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

#chrome browser voor de klok
chrome_options = Options()
# Verwijderd infobars -> bar die liet weten dat het automated was
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
# chrome_options.add_argument("--no-sandbox")
# chrome kios mode -> geen functies zodat de gebruiker niks kan doen
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(options=chrome_options)
# open home pagina

import os

while True:
    oude = ""
    with open('/tmp/.homescreenskilldata/page.txt') as f:
        file = f.read()
        os.system("echo " + file + " > /tmp/test.txt")
        if (file == "\n"):
            oude = "homescreen"
            os.system("echo \"homescreen\" > /tmp/.homescreenskilldata/page.txt")
            driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/homescreen.html")
        if(file == "homescreen" and oude != "homescreen"):
            oude = "homescreen"
            driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/homescreen.html")
        if(file == "clock" and oude != "clock"):
            oude = "clock"
            driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/clock.html")
        else:
            driver.get('file:///opt/mycroft/skills/X-man-homescreen-css/hmm.html')