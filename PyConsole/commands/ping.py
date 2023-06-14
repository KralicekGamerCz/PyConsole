import time
from etc import etc


def cmd():
    ping_start_time = time.time()
    print("pong")
    ping_end_time = time.time()
    ping_response_time = ping_end_time - ping_start_time
    if ping_response_time == 0:
        print("Odezva je: " + etc.green + str(ping_response_time))

    elif ping_response_time > 1:
        print("Odezva je: " + etc.red + str(ping_response_time))

    elif ping_response_time > 0:
        print("Odezva je: " + "\033[93m" + str(ping_response_time))

    else:
        print(etc.red + "Error")

    print("")
