import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import RPi.GPIO as GPIO
import pyrebase

current = 0
on_time = 0
relay_pin = 23
serial_port = '/dev/ttyUSB0'  # Replace with the actual USB port your converter is connected to
baud_rate = 9600

# Connect to the USB to TTL converter
serial_connection = serial.Serial(
    port=serial_port,
    baudrate=baud_rate,
    bytesize=8,
    parity='N',
    stopbits=1,
    xonxoff=0
)
master = modbus_rtu.RtuMaster(serial_connection)
master.set_timeout(2.0)
master.set_verbose(True)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Initialize Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyB1bZ9lXxpZ6u68L24WYWPvywLAFfN3684",
    "authDomain": "check1-580b7.firebaseapp.com",
    "databaseURL": "https://check1-580b7-default-rtdb.firebaseio.com",
    "projectId": "check1-580b7",
    "storageBucket": "check1-580b7.appspot.com",
    "messagingSenderId": "484459339788",
    "appId": "1:484459339788:web:05db8ce8171a7388d4ce29"
}


firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to your Firebase Realtime Database
db = firebase.database()

data_path = "/"  # Set the appropriate data path

while True:
    try:
        # Read data from the USB to TTL converter
        message = [0x01, 0x04, 0x00, 0x00, 0x00, 0x0A]  # Read 10 bytes of data (adjust as needed)
        data = master.execute(1, cst.READ_INPUT_REGISTERS, 0x0000, 10)
        if data:
            current = (data[1] + (data[2] << 8)) / 1000.0  # [A]
            
        time.sleep(10)
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    try:
        # Retrieve data from Firebase
        on_time = db.child(data_path).get().val()
    except Exception as e:
        print(f"Error: {e}")
    
    if current > 0:
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(on_time)  # Assuming on_time is in seconds
        GPIO.output(relay_pin, GPIO.LOW)

