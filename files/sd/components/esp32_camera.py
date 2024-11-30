from esp32 import camera

camera.init(0, {
    "framesize": camera.FRAME_QVGA,  # Set resolution: QVGA = 320x240
    "quality": 10,                   # Image quality: 0 (lowest) to 63 (highest)
    "xclk_freq_hz": 20000000,        # External clock frequency
    "ledc_channel": 0,               # LED control channel (optional)
    "fb_count": 1,                   # Number of frame buffers
    "pin_pwdn": 26,                  # Power down pin
    "pin_reset": 15,                 # Reset pin
    "pin_xclk": 0,                   # XCLK pin
    "pin_sscb_sda": 21,              # I2C SDA
    "pin_sscb_scl": 22,              # I2C SCL
    "pin_d7": 39, "pin_d6": 36,      # Data pins
    "pin_d5": 19, "pin_d4": 18,
    "pin_d3": 5, "pin_d2": 4,
    "pin_d1": 3, "pin_d0": 1,
    "pin_vsync": 25,                 # VSYNC pin
    "pin_href": 23,                  # HREF pin
    "pin_pclk": 21,                  # PCLK pin
})

# Capture an Image
img = camera.capture()
with open('/sd/capture.jpg', 'wb') as f:
    f.write(img)
print("Image captured!")
