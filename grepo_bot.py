import pyautogui
import time
from random import randint


def collect_resources_on_island():
    print("Please select active Grepolis window!")

    time.sleep(3)

    # press space - to get overview of island
    pyautogui.press('space')
    print("Centering on Island...")

    # Click on resource
    pyautogui.click('images/resources.png')
    print("Found village with resources.")

    btn_10min_collect, btn_next_village = get_cords_of_btns()

    for _ in range(6):
        pyautogui.click(btn_10min_collect)
        print("Collected goodies for 10min.")
        time.sleep(randint(1, 2))

        pyautogui.click(btn_next_village)
        print("Visiting next village...")
        time.sleep(randint(1, 2))

    pyautogui.press('escape')
    print("Collected from all villages on this island.")


def get_cords_of_btns():
    # get location of picture 10min_collect
    location_of_10min_collect = pyautogui.locateOnScreen('images/10min_farm_village_button.png')

    # convert to x,y format
    btn_10min_collect = pyautogui.center(location_of_10min_collect)
    print("10min btn found: ", btn_10min_collect)

    # get location of picture next_arrow_farm_village
    location_of_next_village_btn = pyautogui.locateOnScreen('images/next_farm_village_button.png')

    # convert to x,y format
    btn_next_village = pyautogui.center(location_of_next_village_btn)
    print("Next village btn found: ", btn_next_village)

    return btn_10min_collect, btn_next_village


"""
def get_number_of_villages():
    try:
        number_of_villages = int(input("Enter amount of your villages: "))
    except ValueError:
        print("Enter number!")
        get_number_of_villages()

    return number_of_villages


def get_number_of_farm_villages():
    try:
        number_of_farm_villages = int(input("Enter amount of your farm villages: "))
    except ValueError:
        print("Enter number!")
        get_number_of_farm_villages()

    return number_of_farm_villages
"""


def main():
    collect_resources_on_island()


main()
