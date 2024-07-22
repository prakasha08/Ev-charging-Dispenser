import time
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu


# Serial port configuration for the USB to TTL converter
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
            
            voltage = data[0] / 10.0  # [V]
            current = (data[1] + (data[2] << 16)) / 1000.0  # [A]
            power = (data[3] + (data[4] << 16)) / 10.0  # [W]
            energy = data[5] + (data[6] << 16)  # [Wh]
            frequency = data[7] / 10.0  # [Hz]
            power_factor = data[8] / 100.0
            alarm = data[9]  # 0 = no alarm

            print('Voltage [V]: ', voltage)
            print('Current [A]: ', current)
            print('Power [W]: ', power)
            print('Energy [Wh]: ', energy)
            print('Frequency [Hz]: ', frequency)
            print('Power factor: ', power_factor)
            print('Alarm: ', alarm)
            print("--------------------")

       time.sleep(10)
    

    except Exception as e:
        print(f"Error: {str(e)}")


