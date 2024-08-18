import serial
import time

def send_sms(phone_number, message):
    # Open serial connection to SIM808 module
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

    # Wait for the module to initialize
    time.sleep(1)

    # Set SMS mode to text
    ser.write(b'AT+CMGF=1\r\n')
    response = ser.readline().decode('utf-8')
    print(response)
    
    time.sleep(1)
    
    # Set recipient phone number
    ser.write(f'AT+CMGS="{phone_number}"\r\n'.encode('utf-8'))
    response = ser.readline().decode('utf-8')
    print(response)
    
    time.sleep(1)
    # Enter message text
    ser.write(message.encode('utf-8') + b"\r\n")
    
    time.sleep(1)

    # Send Ctrl+Z to indicate end of message
    ser.write(bytes([26]))  # Ctrl+Z character
    time.sleep(1)

    # Read response after sending message
    response = ser.read_all().decode('utf-8')
    print(response)

    # Close serial connection
    ser.close()

# Example usage
send_sms("+919335528194", "Rishit is sad and hasn't take medicine!!")

# import serial
# import time

# def make_call(phone_number):
#     # Open serial connection to SIM808 module
#     ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

#     # Wait for the module to initialize
#     time.sleep(1)

#     # Initiate call
#     ser.write('ATD{};\r\n'.format(phone_number).encode('utf-8'))
#     response = ser.readline().decode('utf-8')
#     print(response)

#     # Close serial connection
#     ser.close()

# # Example usage
# make_call("+919335528194")




