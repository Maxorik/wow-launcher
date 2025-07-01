import subprocess
import pyautogui
import configparser
import ctypes
import time

config = configparser.ConfigParser()
config.read("config.ini")

if __name__ == "__main__":
    # Раскладка должна быть англ
    hkl = ctypes.windll.user32.LoadKeyboardLayoutW(hex(0x0409), 1)

    if config["SETTINGS"]["realmlist"] != '':
        # Изменяем realmlist.wtf
        locale_folder = 'ruRU' if config["SETTINGS"]["locale"] == 'ru' else 'enGB'
        realmlist_file = config["SETTINGS"]["wow_path"] + "\\Data\\" + locale_folder + "\\realmlist.wtf"
        with open(realmlist_file, 'w') as file:
            print(f"Realmlist изменен на {config["SETTINGS"]["realmlist"]}...")
            file.write(config["SETTINGS"]["realmlist"])

    ctypes.windll.user32.PostMessageW(0xFFFF, 0x0050, 0, hkl)
    time.sleep(1)

    # Запускаем wow.exe и вводим креды
    print("Запуск wow.exe...")
    exe_path = config["SETTINGS"]["wow_path"] + '\\Wow.exe'
    subprocess.Popen(exe_path)
    time.sleep(int(config["SETTINGS"]["loading_time"]))
    ctypes.windll.user32.ActivateKeyboardLayout(hkl, 0)

    pyautogui.write(config["SETTINGS"]["login"])
    pyautogui.press('tab')
    pyautogui.write(config["SETTINGS"]["password"])
    pyautogui.press('enter')


