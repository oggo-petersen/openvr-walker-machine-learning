from utils.trainer import Trainer
from utils.keypress import send_current_state
from server import SocketServer

# Variables used.
csv_handler = None
trainer = None


def predict_movement(esp32_data):
    # Appends data from the socket and guesses the current state of the player.
    trainer.append_new_data(esp32_data)
    current_state = trainer.predict()

    # Sends current state to our steamVR driver.
    send_current_state(current_state)
    print(current_state)


if __name__ == "__main__":
    # Loads trainer with selected joblib file.
    trainer = Trainer('train-data')

    server = SocketServer(8080)
    server.start_socket()
    server.run_socket(predict_movement)
