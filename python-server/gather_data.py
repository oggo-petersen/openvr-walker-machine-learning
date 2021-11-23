import os
import time

from server import SocketServer
from utils.csv_handler import CSVHandler
from utils.consts import IDLE, MOVING

# For gathering data - set current state.
current_state = MOVING

# Ensure gathered_data folder exists.
if not os.path.exists('gathered_data'):
    os.makedirs('gathered_data')

# Variables used.
csv_handler = CSVHandler('gathered_data/gathering_idle.csv')
amount_of_rows_to_persist = 2000


def gather_data(esp32_data):
    global csv_handler
    global amount_of_rows_to_persist

    accelX, accelY, accelZ, gyroX, gyroY, gyroZ = esp32_data

    csv_handler.write_row([accelX, accelY, accelZ, gyroX, gyroY, gyroZ, current_state])
    amount_of_rows_to_persist -= 1
    print(amount_of_rows_to_persist)

    if amount_of_rows_to_persist <= 0:
        exit()



if __name__ == "__main__":
    csv_handler.gather_data()

    # Give 5 secs to prepare.
    time.sleep(5)

    server = SocketServer(8080)
    server.start_socket()
    server.run_socket(gather_data)
