import time
from commands.etc import colors


def cmd():
    ping_start_time = time.time()
    print("pong")
    ping_end_time = time.time()
    ping_response_time = ping_end_time - ping_start_time
    if ping_response_time == 0:
        print("Odezva je: " + colors.green + str(ping_response_time))

    elif ping_response_time > 1:
        print("Odezva je: " + colors.red + str(ping_response_time))

    elif ping_response_time > 0:
        print("Odezva je: " + "\033[93m" + str(ping_response_time))

    else:
        print(colors.red + "Error")

    print("")
