import serial
import time
import sys

def test_leds():
    """Test LEDs directly without needing Arduino code upload"""
    
    # LED sequence matching your assembly
    led_sequence = [
        0b0000000001,  # LED 0
        0b0000000010,  # LED 1
        0b0000000100,  # LED 2
        0b0000001000,  # LED 3
        0b0000010000,  # LED 4
        0b0000100000,  # LED 5
        0b0001000000,  # LED 6
        0b0010000000,  # LED 7
        0b0100000000,  # LED 8
        0b1000000000,  # LED 9
        0b0000000000,  # All OFF
    ]
    
    # Try to connect to Arduino
    try:
        ser = serial.Serial('COM3', 115200, timeout=1)
        time.sleep(2)  # Wait for Arduino to reset
        print("Connected to Arduino")
        
        for i, pattern in enumerate(led_sequence):
            print(f"LED {i if i < 10 else 'ALL OFF'} - Pattern: {pattern:010b}")
            
            # Send the pattern
            data = bytes([pattern & 0xFF, (pattern >> 8) & 0xFF])
            ser.write(data)
            
            # Wait for acknowledgment
            ack = ser.read(1)
            if ack == b'\xAA':
                print("  ✓ Acknowledged")
            else:
                print("  ✗ No acknowledgment")
            
            time.sleep(1)  # 1 second delay
            
        ser.close()
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nIf Arduino is not programmed, let's use Method 1 with Arduino IDE first.")

if __name__ == "__main__":
    test_leds()