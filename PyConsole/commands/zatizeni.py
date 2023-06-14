import time
import os
from etc import etc


def cmd():
    zatizeni_start_time = time.time()
    print(999999 * "000000000" + etc.reset)
    zatizeni_end_time = time.time()
    os.system('cls')
    etc.welcome()
    zatizeni_response_time = zatizeni_end_time - zatizeni_start_time
    if zatizeni_response_time < 1:
        print("Odezva je: " + etc.green + str(zatizeni_response_time))

    elif zatizeni_response_time < 2:
        print("Odezva je: " + etc.red + str(zatizeni_response_time))

    elif zatizeni_response_time < 3:
        print("Odezva je: " + "\033[93m" + str(zatizeni_response_time))

    else:
        print(etc.red + "Error")

    print("")
