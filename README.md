# openvr-walker-machine-learning

An openVR driver with python and ESP32 with a MPU-6050 module.
Here we use a machine learning algorithm (ExtraTreesClassifier) to predict wether we are moving or standing still.

# Running Python

If you want to gather data, run `python3 gather_data.py`
If you want to train and persist your model, run `python3 create_model.py`
If you want to use the controller, run `esp32_controller.py`

# Open VR Driver

I suggest you follow the tutorial made by FinallyFunctional, which can be found here:
[https://github.com/finallyfunctional/openvr-driver-example](https://github.com/finallyfunctional/openvr-driver-example)
For simplicity, I've added my changed files to `openvr-driver` folder so that you can use them as well.
All credits go to FinallyFunctional for such an amazing work!

# ESP32 Compiling & Running

Install ADAFruit MPU6050 driver in Arduino IDE.
Don't forget to put your wifi details and the ip from the machine that is running your python server, as well your VR games!

## More can be found in my article!
-[Petersen Projects | Walking in VR with ESP32](https://petersen-projects.com/?p=78)