import camera

## ESP32-CAM (default configuration) - https://bit.ly/2Ndn8tN
camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)

## M5Camera (Version B) - https://bit.ly/317Xb74
camera.init(0, d0=32, d1=35, d2=34, d3=5, d4=39, d5=18, d6=36, d7=19,
            format=camera.JPEG, framesize=camera.FRAME_VGA, xclk_freq=camera.XCLK_10MHz,
            href=26, vsync=25, reset=15, sioc=23, siod=22, xclk=27, pclk=21, fb_location=camera.PSRAM)   #M5CAMERA

## T-Camera Mini (green PCB) - https://bit.ly/31H1aaF
import axp202 # source https://github.com/lewisxhe/AXP202_PythonLibrary
# USB current limit must be disabled (otherwise init fails)
axp=axp202.PMU( scl=22, sda=21, address=axp202.AXP192_SLAVE_ADDRESS  )
limiting=axp.read_byte( axp202.AXP202_IPS_SET )
limiting &= 0xfc
axp.write_byte( axp202.AXP202_IPS_SET, limiting )

camera.init(0, d0=5, d1=14, d2=4, d3=15, d4=18, d5=23, d6=36, d7=39,
            format=camera.JPEG, framesize=camera.FRAME_VGA, 
            xclk_freq=camera.XCLK_20MHz,
            href=25, vsync=27, reset=-1, pwdn=-1,
            sioc=12, siod=13, xclk=32, pclk=19)

# The parameters: format=camera.JPEG, xclk_freq=camera.XCLK_10MHz are standard for all cameras.
# You can try using a faster xclk (20MHz), this also worked with the esp32-cam and m5camera
# but the image was pixelated and somehow green.

## Other settings:
# flip up side down
camera.flip(1)
# left / right
camera.mirror(1)

# framesize
camera.framesize(camera.FRAME_240x240)
# The options are the following:
# FRAME_96X96 FRAME_QQVGA FRAME_QCIF FRAME_HQVGA FRAME_240X240
# FRAME_QVGA FRAME_CIF FRAME_HVGA FRAME_VGA FRAME_SVGA
# FRAME_XGA FRAME_HD FRAME_SXGA FRAME_UXGA FRAME_FHD
# FRAME_P_HD FRAME_P_3MP FRAME_QXGA FRAME_QHD FRAME_WQXGA
# FRAME_P_FHD FRAME_QSXGA
# Check this link for more information: https://bit.ly/2YOzizz

# special effects
camera.speffect(camera.EFFECT_NONE)
# The options are the following:
# EFFECT_NONE (default) EFFECT_NEG EFFECT_BW EFFECT_RED EFFECT_GREEN EFFECT_BLUE EFFECT_RETRO

# white balance
camera.whitebalance(camera.WB_NONE)
# The options are the following:
# WB_NONE (default) WB_SUNNY WB_CLOUDY WB_OFFICE WB_HOME

# saturation
camera.saturation(0)
# -2,2 (default 0). -2 grayscale 

# brightness
camera.brightness(0)
# -2,2 (default 0). 2 brightness

# contrast
camera.contrast(0)
#-2,2 (default 0). 2 highcontrast

# quality
camera.quality(10)
# 10-63 lower number means higher quality

buf = camera.capture()
