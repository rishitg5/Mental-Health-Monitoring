import cv2
import numpy as np
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


# Read the image
#image = cv2.imread('/home/rishit/Project/coins.jpg')
image = cv2.imread('/home/rishit/Downloads/test.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#number of pills in cartridge yesterday
c = 5

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (11, 11), 0)

# Apply Canny edge detection
canny = cv2.Canny(blur, 30, 150)

# Dilate the edges to close gaps
dilated = cv2.dilate(canny, None, iterations=2)

# Find circles using Hough Circle Transform
circles = cv2.HoughCircles(
    dilated, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=1000)

# Check if circles were detected
if circles is not None:
    # Convert circles to integer coordinates
    circles = np.uint16(np.around(circles))
    
    # Get the number of detected circles
    num_circles = circles.shape[1]
    print(f"Number of pills detected: {num_circles}")
    
    if num_circles >= c:#send_sms("+919335528194", "Rishit is sad and hasn't take medicine!!")
        print(f"The person has not taken medicine.")
    else:
        print(f"The person has taken medicine.")
        
else:
    print("No pills detected.")
