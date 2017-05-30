# multi-pi-videoplayer

A set of python script to control multiple videos on multiple raspberry pi's from a single server Pi. There are many methods to do parts of this but nothing simple and complete that I found. The goal for this project is a complete how-to setup for controlling multiple Pi's for use in art installations or kiosk type applications.

# H1 Setting up the clients

I suggest setting up one Pi with all of the functions working and then cloning it using rpi-clone [link](https://github.com/billw2/rpi-clone). You may consider turning off screen blanking in the /etc/X11/xorg.conf file for all the machines

1. The open_videos.py script assumes that a usb stick is mounted to /mnt/usb in each client Pi [link](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=38058)
2. The usb drive should have a folder called 'media' on the root level, and the subfolder as indicated in the script
3. The drive should be automatically mounted in that directory
   * sudo nano /etc/fstab
   * then add the line to the end
   * /dev/sda1 /mnt/usb vfat defaults,nofail 0 2
   * This will assumes there is only one drive plugged into the Pi.
 4. The server and pi's should be on the same wifi network, and I am using standard dhcp (no static ip's)
 5. Set up the Pi's to allow ssh logging in without passwords [link](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
 6. Set each client to allow empty passwords
    * sudo nano /etc/ssh/sshd_config
 7. Create the necessarry ~/.ssh directory
    * cd ~
    * install -d -m 700 ~/.ssh
 8. Set up hostname in raspi-config on each client to 'client0', 'client1', etc.
 9. Install omxplayer and put the dbuscontrol.sh script on the root ~ [link](https://github.com/popcornmix/omxplayer/)

 
 # H1 Setting up the server
  
  1. Install ParallelSSH on the server pi [link](https://github.com/ParallelSSH/parallel-ssh)
  2. Generate ssh keys and copy to the client machines [link](https://www.raspberrypi.org/documentation/remote-access/ssh/passwordless.md)
     * ssh-keygen -t rsa -C pi@client0.local
     * cat ~/.ssh/id_rsa.pub | ssh pi@client0.local 'cat >> .ssh/authorized_keys'
   3. If you are going to run the GPIO examples with physical buttons, install pygame


