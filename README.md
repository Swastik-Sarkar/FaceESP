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
6. [How to Run](#how-to-run)

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
