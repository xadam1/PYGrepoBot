import pyautogui
import time
import random


def get_cities():
    """
    Gets input from user - number of cities per each island

    :return: list of number of cities per island, each element represents one island
    """
    island_num = 1
    print("You will be asked to input number of cities on each of your islands.\n"
          "GrepoBot needs this information to be able to loop over all villages.\n\n"
          "If you have no more cities press 'q' to stop this.\n"
          "And if you fucked up, press 'n'\n")

    cities_per_island = []

    while True:
        pressed_key = input("Cities on {}. island: \t".format(island_num))
        island_num += 1

        if pressed_key == 'n':
            print("Resetting...")
            # set to 2 bcs except will reduce by 1
            island_num = 2
            cities_per_island = []

        if pressed_key == 'q':
            print("Ok, thank you!")
            break

        try:
            count = int(pressed_key)
            cities_per_island.append(count)

        except ValueError:
            print("Unknown command! Try again...")
            island_num -= 1

    return cities_per_island


def collect_countdown_loop(cities_on_island):
    # collect, move to other island, wait 11 mins

    while True:
        for island in cities_on_island:
            # collect on this island
            collect_resources_on_island(1)

            print("Moving to another island!\n")
            # switch to other island
            for _ in range(island):
                pyautogui.press('right')
                time.sleep(0.3)

        sleep_time = round(random.randint(660, 900), 2)
        print("\nNow waiting for {}mins\nThis can differ every harvest\n".format(sleep_time / 60))
        time.sleep(sleep_time)


def collect_resources_on_island(farm_duration):
    """
    Loops through each farm village on current island, and collect resources from each one of them

    :param farm_duration: int type representing what type of farming should be used
    :return: nothing, collects resources from villages
    """
    # Create dictionary with images
    collect_dict = {1: 'images/quick_farm_btn.png',
                    2: 'TODO'}

    # set img path to desired type of pic
    collect_type = collect_dict[farm_duration]

    time.sleep(2)

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
    print("Successfully collected resources on this island!")


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
    collect_type = int(input("What type of computer are you on?\n"
                             "[1]: Faster ... almost instant loading of windows\n"
                             "[2]: Slower ... VMs or older computers - NOT IMPLEMENTED YET\n"
                             "--->>>\t"))
    return collect_type


def main():
    """
    Main function, starts when Bot is executed

    :return: not determined yet, probably nothing
    """

    print("Welcome to GrepoBot!\n")

    # Get speed of computer from user
    # pc_speed = get_input_init()

    # Get list of num of cities on each island
    cities_per_island = get_cities()

    print("Please select active Grepolis browser window!")

    collect_countdown_loop(cities_per_island)


main()
