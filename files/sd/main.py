import sys
import time
from hardware import setup_hardware, recognize_face, register_face, clear_faces
from oled import display_message

sys.path.append("/sd/components")
setup_hardware()

def main():
    while True:
        display_message("System Ready", "Waiting...")
        recognize_face()

if __name__ == "__main__":
    main()
