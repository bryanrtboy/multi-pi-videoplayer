# multi-pi-videoplayer

A set of python script to control multiple videos on multiple raspberry pi's from a single server Pi. There are many methods to do parts of this but nothing simple and complete that I found. The goal for this project is a complete how-to setup for controlling multiple Pi's for use in art installations or kiosk type applications.

# H1 Setting up the clients

1. The open_videos.py script assumes that a usb stick is mounted to /mnt/usb in each client Pi [link](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=38058)
2. The usb drive should have a folder called 'media' on the root level, and the subfolder as indicated in the script
3. The drive should be automatically mounted in that directory
  * sudo nano /etc/fstab
  * then add the line to the end
  * /dev/sda1 /mnt/usb vfat defaults,nofail 0 2
  * This will assumes there is only one drive plugged into the Pi.
  
  


