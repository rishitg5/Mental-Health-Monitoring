import speech_recognition as sr
import paramiko
from scp import SCPClient

recognizer = sr.Recognizer()

def write_string_to_file(file_path, text_string):
    try:
        with open(file_path, 'w') as file:
            file.write(text_string)
        print("Text string successfully written to", file_path)
    except Exception as e:
        print("An error occurred:", e)

with sr.Microphone() as source:
    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message...')
    recorded_audio = recognizer.listen(source)
    print('Done recording..')


# Replace 'Your text string here' with the text you want to write to the file
# text_string = 'Your text string here'


try:
    print('Printing the message..')
    text = recognizer.recognize_google(recorded_audio, language='en-US')
    print('Your message: {}'.format(text))

except Exception as ex:
    print(ex)

# Replace 'your_file.txt' with the path where you want to save the text file
file_path = './audio.txt'

# Call the function to write the text string to the file
write_string_to_file(file_path, text)

def send_file_to_raspi(local_file_path, remote_file_path, raspi_ip, username, ssh_key_path, ssh_key_passphrase):
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load SSH private key with passphrase
        private_key = paramiko.RSAKey.from_private_key_file(ssh_key_path, password=ssh_key_passphrase)

        # Connect to Raspberry Pi
        ssh_client.connect(hostname=raspi_ip, username=username, pkey=private_key)

        # SCP the file to Raspberry Pi
        with SCPClient(ssh_client.get_transport()) as scp_client:
            scp_client.put(local_file_path, remote_file_path)

        print("File sent successfully to Raspberry Pi")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close SSH connection
        if ssh_client:
            ssh_client.close()

# Replace 'your_username' with your Raspberry Pi username
username = "rishit"

# Replace 'your_raspi_ip' with the IP address of your Raspberry Pi
raspi_ip = "rishit"

# Replace 'your_local_file_path' with the path to the file on your laptop
local_file_path = "./audio.txt"

# Replace 'your_remote_file_path' with the directory path on your Raspberry Pi where you want to save the file
remote_file_path = "~/Project/"

# Replace 'your_ssh_key_path' with the path to your SSH private key
ssh_key_path = "C:/Users/Anuraj Bhaskar/.ssh/id_rsa"

# Replace 'your_ssh_key_passphrase' with the passphrase for your SSH private key
ssh_key_passphrase = "deeznuts"

# Call the function to send the file to Raspberry Pi
send_file_to_raspi(local_file_path, remote_file_path, raspi_ip, username, ssh_key_path, ssh_key_passphrase)