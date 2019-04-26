import pyautogui
import time
import random


def collect_resources_on_island(farm_duration):
    """
    Loops through each farm village on island, and collect resources from each one of them

    :param farm_duration: int type representing what type of farming should be used
    :return: nothing, collects resources from villages
    """
    # Create dictionary with images
    collect_dict = {1: 'images/quick_farm_btn.png',
                    2: 'TODO'}

    # set img path to desired type of pic
    collect_type = collect_dict[farm_duration]

    print("Please select active Grepolis browser window!")

    time.sleep(3)

    # press space - to get overview of island
    pyautogui.press('space')
    print("Centering on Island...")

    time.sleep(1)

    # Opens collect from village window
    pyautogui.click('images/resources.png')
    print("Found village with resources.")

    # Find buttons and save the positions
    btn_collect = get_cords_of_btn(collect_type)
    btn_next_village = get_cords_of_btn('images/next_farm_village_button.png')

    print("Collecting your goodies!")
    for _ in range(6):
        pyautogui.click(btn_collect)

        # sleeps for (0.3 - 1.3 sec) - rounded random on 2 digits (0.00 - 1.00) + 0.3 sec
        time.sleep(round(random.random(), 2) + 0.3)

        pyautogui.click(btn_next_village)

        time.sleep(round(random.random(), 2) + 0.3)

    pyautogui.press('escape')
    print("Successfully collected resources from villages on this island, boss!")


def get_cords_of_btn(btn_picture):
    """
    Just locate the picture passed as a parameter

    :param btn_picture: .png picture of btn that should be found
    :return: x,y cords to click on the desired button
    """

    # get btn position
    square_location_btn = pyautogui.locateOnScreen(btn_picture, 5)

    # convert to x,y format
    btn_position = pyautogui.center(square_location_btn)

    print("DEBUG: found btn_location:\t", btn_position)

    return btn_position


def get_input_init():
    """
    Quick function to get user input of wanted farming mode

    :return: int type representing farming mode
    """
    # Get input from user for type of farming
    collect_type = int(input("What type of farming do you want to start?\n"
                             "[1]: Short (every 10min)\n"
                             "[2]: Longer ... not implemented yet ->\t"))
    return collect_type


def main():
    """
    Main function, starts when Bot is executed

    :return: not determined yet, probably nothing
    """

    print("Welcome to farming GrepoBot!\n\n")

    # Get type of desired farming
    collect_duration = get_input_init()

    collect_resources_on_island(collect_duration)


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

main()
