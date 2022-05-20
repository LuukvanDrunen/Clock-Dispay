#Het includen/invoegen van benodigden libraries

# from calendar import c
import os
from mycroft import MycroftSkill, intent_file_handler


class ClockForSchoolDieWantIi(MycroftSkill):
    
        
    # maakt listener aan die checkt wanneer het bestand voor de homescreen change veranderd
    os.system('mkdir /tmp/.homescreenskilldata/ 2>/dev/null')
    os.system("echo \"\" > /tmp/.homescreenskilldata/page.txt")
    os.system('python3 /opt/mycroft/skills/clock-for-school-die-want-ii-skill/screenChanger.py >> /tmp/.homescreenskilldata/fileChecker.log &')
    
    def __init__(self):
        MycroftSkill.__init__(self)
        
    #Het bestand van commands die klok laten zien
    @intent_file_handler('ii.want.die.school.for.clock.intent')

    #de functie die mycroft runt wanneer de gebruiker erom gevraagd heeft
    def handle_ii_want_die_school_for_clock(self, message):
        print(os.system("cat /proc/self/environ >> /tmp/test.txt"))

        #Verteld de gebruiker na het activeren van clock command dat de klok op gaat starten
        self.speak_dialog('ii.want.die.school.for.clock')

        with open('/tmp/.homescreenskilldata/page.txt', 'w') as f:
            f.write('clock')
        
        

#verteld aan mycroft de juiste function name voor deze skill
def create_skill():

    return ClockForSchoolDieWantIi()