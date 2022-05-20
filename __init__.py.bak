#Het includen/invoegen van benodigden libraries

from calendar import c
from mycroft import MycroftSkill, intent_file_handler

##pip install nog?
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## NOTES
## wat nou als we de driver variable blok stuk alles globaal maken, ergens in mycroft gedifned
## dan kunnen we, wanneer we een skill callen, de driver page veranderen (?)
## fking kut selenium


class ClockForSchoolDieWantIi(MycroftSkill):
    print("FDGHJKFGHFHJKHGFHJKHGFDFGHJKJHGFDFGHJKJHGFDFGHJKLJHGFDFGHJKLJHGFDGHJKHGFGHJK")
    
     #chrome browser voor de klok
    chrome_options = Options()

    # Verwijderd infobars -> bar die liet weten dat het automated was
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

    # chrome kios mode -> geen functies zodat de gebruiker niks kan doen
    # chrome_options.add_argument("--kiosk")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # open home pagina
    driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/homescreen.html")
    
    
    def __init__(self):
        MycroftSkill.__init__(self)

    ##we moeten eig. bij elke lijn neer zetten wat het doen
    ##later handig voor presentaties

    #Het bestand van commands die klok laten zien
    @intent_file_handler('ii.want.die.school.for.clock.intent')

    #de functie die mycroft runt wanneer de gebruiker erom gevraagd heeft
    def handle_ii_want_die_school_for_clock(self, message):

        #Verteld de gebruiker na het activeren van clock command dat de klok op gaat starten
        self.speak_dialog('ii.want.die.school.for.clock')


#verteld aan mycroft de juiste function name voor deze skill
def create_skill():
    
    return ClockForSchoolDieWantIi()