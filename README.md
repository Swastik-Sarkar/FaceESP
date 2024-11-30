---

# **ESP32-S3 Face Recognition with SD Card Execution**

A comprehensive guide to building a self-contained face recognition system using the **ESP32-S3**, MicroPython, an OLED display, and SD card execution. Btw dont forget to star this <3

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Hardware Requirements](#hardware-requirements)
3. [Software Requirements](#software-requirements)
4. [File Structure](#file-structure)
5. [MicroPython Installation](#micropython-installation)
6. [Code Overview](#code-overview)
    - [Bootloader Script](#bootloader-script)
    - [Main Program](#main-program)
    - [Components](#components)
7. [How to Run](#how-to-run)

---

## **Introduction**
This project implements a face recognition system using **ESP32-S3**. It dynamically loads Python scripts and executes them directly from an SD card, enabling easy updates without re-flashing. 

**Features**:
- Face recognition with an ESP32-S3 camera module.
- Modular components (OLED, SD card, GPIO buttons).
- Supports four modes:
  - **On/Off**: Long press to toggle power.
  - **Register**: Capture and register a new face.
  - **Cancel**: Exit registration mode.
  - **Clear**: Delete all registered faces.

---

## **Hardware Requirements**

| **Component**       | **Quantity** | **Description**                     |
|---------------------|--------------|-------------------------------------|
| ESP32-S3 Board      | 1            | With built-in or external camera.  |
| Micro SD Card + Adapter | 1        | To store Python files.             |
| SD Card Module      | 1            | For SD card interfacing.           |
| OLED Display        | 1            | I2C-based, SSD1306 128x64.         |
| Buttons             | 4            | For On/Off, Register, Cancel, Clear. |
| LEDs                | 2            | Green and Red LEDs.                |
| Buzzer              | 1            | For audio feedback.                |
| Resistors           | As needed    | For button pull-up/down circuits.  |
| Jumper Wires        | Several      | For connections.                   |
| Power Supply        | 1            | ESP32-compatible (e.g., 5V via USB).|

---

## **Software Requirements**

### **1. Firmware**
- [MicroPython for ESP32-S3](https://micropython.org/download/esp32/).

### **2. Python Tools**
Install these tools on your computer:
```bash
pip install esptool adafruit-ampy mpremote rshell micropython-uasyncio
```

### **3. Libraries for Components**
Place these files in the `/sd/components/` directory:
- **`ssd1306.py`**: [OLED Display Driver](https://github.com/micropython/micropython/tree/master/drivers/display).
- **`esp32_camera.py`**: Camera handling for face recognition (use [custom camera build](https://github.com/lemariva/micropython-camera-driver)).
- **`hardware.py`**: Handles GPIO, buttons, LEDs, and buzzer.

---

## **File Structure**

Organize the SD card as follows:

```
/sd/
  ├── main.py             # Main program
  ├── components/         # Component drivers and utilities
  │   ├── ssd1306.py      # OLED driver
  │   ├── esp32_camera.py # Camera logic
  │   ├── hardware.py     # Buttons, LEDs, and buzzer
  └── data/               # Registered face data
      ├── encodings/
```

---

## **MicroPython Installation**

### **Step 1: Download MicroPython**
Download the appropriate MicroPython firmware for ESP32-S3 from [here](https://micropython.org/download/esp32/).

### **Step 2: Flash the Firmware**
1. Install `esptool`:
   ```bash
   pip install esptool
   ```
2. Erase existing firmware:
   ```bash
   esptool.py --chip esp32 erase_flash
   ```
3. Flash MicroPython:
   ```bash
   esptool.py --chip esp32 write_flash -z 0x1000 micropython.bin
   ```

---

## **Code Overview**

### **1. Bootloader Script (`boot.py`)**
Resides in ESP32 flash. Mounts the SD card and runs `main.py`:
```python
import os
import sdcard
from machine import Pin, SPI

# SD Card Initialization
spi = SPI(2, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
sd = sdcard.SDCard(spi, Pin(15))
os.mount(sd, "/sd")

# Run main.py
MAIN_PROGRAM = "/sd/main.py"
if os.path.exists(MAIN_PROGRAM):
    with open(MAIN_PROGRAM) as f:
        exec(f.read())
else:
    print("main.py not found on SD card.")
```

---

### **2. Main Program (`main.py`)**
Manages logic and imports components:
```python
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
```

---

### **3. Component Code**

#### **Hardware Control (`hardware.py`)**
Handles GPIO, LEDs, buttons, and buzzer:
```python
from machine import Pin

# GPIO Pins
GREEN_LED = 15
RED_LED = 16
BUZZER = 17
BUTTON_ON_OFF = 18

green_led = Pin(GREEN_LED, Pin.OUT)
red_led = Pin(RED_LED, Pin.OUT)
buzzer = Pin(BUZZER, Pin.OUT)

def setup_hardware():
    green_led.off()
    red_led.off()
    buzzer.off()

def recognize_face():
    green_led.on()
    time.sleep(1)
    green_led.off()
```

#### **OLED Display (`ssd1306.py`)**
Displays messages:
```python
from machine import I2C, Pin
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def display_message(line1, line2=""):
    oled.fill(0)
    oled.text(line1, 0, 0)
    oled.text(line2, 0, 16)
    oled.show()
```

---

## **How to Run**

1. **Prepare the SD Card**:
   - Copy `main.py` and the `components/` folder to the SD card.

2. **Insert SD Card**:
   - Insert the SD card into the SD card module.

3. **Power On ESP32**:
   - Long press the On/Off button.

4. **Modes**:
   - **Normal Mode**: Detects faces.
   - **Register Mode**: Add a new face.
   - **Clear Mode**: Deletes all faces.

5. **Debug**:
   - Use a serial terminal to monitor output.

---
