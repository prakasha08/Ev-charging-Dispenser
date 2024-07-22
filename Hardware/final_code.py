import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import RPi.GPIO as GPIO
import pyrebase
GPIO.setmode(GPIO.BCM)

current=0
on_time=0
relay_pin=23
GPIO.setup(relay_pin, GPIO.OUT)
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


data_path = "/hii"  
try:
    # Retrieve data from Firebase
       data1 = db.child(data_path).get().val()
       print(data1)
except Exception as e:
       print(f"Error: {e}")
GPIO.output(relay_pin, GPIO.LOW)
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

while True:
    try:
        # Read data from the USB to TTL converter
       message = [0x01,0x04,0x00,0x00,0x00,0x0A]  # Read 10 bytes of data (adjust as needed)
        
       data = master.execute(1,cst.READ_INPUT_REGISTERS,0x0000,10)
       if data:
            
            
            current = (data[1] + (data[2] << 16)) / 1000.0  # [A]
            
            break
       time.sleep(1)
       print("hii")
     
        

    except Exception as e:
        print()
    


while current>0:
       
       time.sleep(data1-2)
       GPIO.output(relay_pin, GPIO.HIGH)





            