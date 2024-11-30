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
| OV2640 Cam Module   | 1            | Camera module used for this project. |

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
---

## **Steps to Add OV2640 to ESP32**

### **1. Hardware Connections**
The OV2640 camera module has several pins that need to be connected to the ESP32. Here's a common pin mapping:

| **OV2640 Pin** | **ESP32 Pin** (Example) | **Description**       |
|----------------|--------------------------|-----------------------|
| `VCC`          | 3.3V                    | Power supply (3.3V).  |
| `GND`          | GND                     | Ground.               |
| `D0 - D7`      | GPIO32-GPIO39           | Data lines.           |
| `XCLK`         | GPIO0                   | Clock signal.         |
| `PCLK`         | GPIO21                  | Pixel clock.          |
| `VSYNC`        | GPIO25                  | Vertical sync.        |
| `HREF`         | GPIO23                  | Horizontal sync.      |
| `SCL`          | GPIO22                  | I2C clock.            |
| `SDA`          | GPIO21                  | I2C data.             |
| `RESET`        | GPIO15 (Optional)       | Reset pin.            |
| `PWDN`         | GPIO26 (Optional)       | Power down (optional).|

- Use jumper wires or a dedicated ESP32 camera development board (e.g., ESP32-CAM) for connection.
- Double-check pin assignments for your specific ESP32-S3 development board, as they may vary.

---

### **2. MicroPython Firmware**
Ensure you are using a MicroPython firmware version that supports the camera interface. Here’s how to get started:

#### **Download Camera-Compatible Firmware**
- Use a MicroPython build with camera support, such as:
  - [MicroPython Camera Firmware by Loboris](https://github.com/lemariva/micropython-camera-driver).
  - Official ESP32-CAM firmware (check documentation for camera support).

#### **Flash Firmware**
Follow the same process as flashing standard MicroPython firmware:
```bash
esptool.py --chip esp32 write_flash -z 0x1000 camera_firmware.bin
```

---

### **4. Troubleshooting**
- **Black Image or No Output:**
  - Ensure `framesize` and `quality` settings match your camera module's capability.
  - Verify pin connections and mappings.
  - Check the power supply (some cameras require a stable 3.3V).

- **Camera Initialization Fails:**
  - Double-check the firmware compatibility with OV2640.
  - Try reducing the `xclk_freq_hz` value (e.g., 10 MHz).

- **Error: `camera` module not found**:
  - Ensure you have flashed a camera-compatible MicroPython firmware.

---

### **5. Alternative: ESP-IDF for Advanced Control**
For more advanced control or performance, consider using the **ESP-IDF framework** with native ESP32-CAM libraries, as it provides full support for OV2640.

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
