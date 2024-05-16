import minimalmodbus
import time
# Define the device address and serial port
device_address =1  # Address code 
serial_port = '/dev/tty.usbserial-AU06CSVO'

# Create a Modbus instrument
instrument = minimalmodbus.Instrument(serial_port, device_address)
instrument.serial.baudrate = 4800
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.1 # seconds


# Define the data address and the number of registers to read
data_address =0 # Starting address 
number_of_registers = 4


# Function code for reading holding registers is 3
function_code = 3 # function code 
# Read data from the Modbus device
while True:
    try:
        print("==================")
        data = instrument.read_registers(data_address, number_of_registers, function_code)
        print(f"Read data: {hex(data[0]), hex(data[1]) , hex(data[2]), hex(data[3]) } ")
        print(f"Read data: {data }")
        time.sleep(1)
    except minimalmodbus.ModbusException as e:
        print(f"Modbus error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# import minimalmodbus

# # Define the Modbus device address and serial port
# device_address = 1  # Change this to your device's address
# serial_port = '/dev/tty.usbserial-AU06CSVO'  # Change this to your serial port

# # Create a Modbus instrument
# instrument = minimalmodbus.Instrument(serial_port, device_address)
# instrument.serial.baudrate = 4800 # Set your baud rate
# instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
# instrument.serial.stopbits = 1

# # Define the Modbus function code for reading holding registers (adjust as needed)
# function_code = 0x03

# # Define the Modbus register addresses for wind data (adjust as needed)
# wind_speed_register = 0x00
# wind_direction_register = 0x01

# try:
#     # Read wind speed and direction
#     wind_speed = instrument.read_register(wind_speed_register, function_code)
#     wind_direction = instrument.read_register(wind_direction_register, function_code)

#     print(f"Wind Speed: {wind_speed} m/s")
#     print(f"Wind Direction: {wind_direction} degrees")
# except minimalmodbus.ModbusException as e:
#     print(f"Modbus error: {e}")
# except Exception as e:
#     print(f"Error: {e}")














