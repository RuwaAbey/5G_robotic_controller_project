import serial
import time

SERIAL_PORT = 'COM24'  
BAUD_RATE = 115200 

def send_at_command(command, modem, delay=1):
    
    modem.write((command + '\r').encode()) 
    time.sleep(delay)  
    response = modem.read_all().decode('utf-8', errors='ignore')  
    return response

def main():
    try:
        
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5) as modem:
            print("Modem connected successfully. Type 'exit' to quit.")

            while True:
                
                at_command = input("Enter AT command: ")

                if at_command.lower() == 'exit':
                    print("Exiting.")
                    break


                response = send_at_command(at_command, modem)
                print(f"Response:\n{response}")

    except serial.SerialException as e:
        print(f"Failed to connect to the modem: {e}")

if __name__ == "__main__":
    main()
