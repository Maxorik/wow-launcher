import subprocess
import pyautogui
import configparser
import time

config = configparser.ConfigParser()
config.read("config.ini")

if __name__ == "__main__":
    if config["SETTINGS"]["realmlist"] != '':
        # Изменяем realmlist.wtf
        locale_folder = 'ruRU' if config["SETTINGS"]["locale"] == 'ru' else 'enGB'
        realmlist_file = config["SETTINGS"]["wow_path"] + "\\Data\\" + locale_folder + "\\realmlist.wtf"
        with open(realmlist_file, 'w') as file:
            file.write(config["SETTINGS"]["realmlist"])

    # Запускаем wow.exe и вводим креды
    exe_path = config["SETTINGS"]["wow_path"] + '\\Wow.exe'
    subprocess.Popen(exe_path)
    time.sleep(int(config["SETTINGS"]["loading_time"]))

    pyautogui.write(config["SETTINGS"]["login"])
    pyautogui.press('tab')
    pyautogui.write(config["SETTINGS"]["password"])
    pyautogui.press('enter')


