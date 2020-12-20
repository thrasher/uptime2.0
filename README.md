# Pi-UpTime2.0 and PiZ-UpTime 2.0
*Last Update December 20, 2020.*

To monitor the battery and shutdown the pi automatically every time the Pi reboots, follow the steps below.

1) Save the python scripts you have downloaded in a folder called uptime (or any other name). We will use
   uptime for this example. Note the path using the "pwd" command. We will assume the path for the folder is
   /home/pi/uptime and all the files are in that folder. Use the file **uptime-2.0-rc.local.py**
   * Please edit the lines in the file which measures termperature. The code for temperature measurement is different
     for PiZ-UpTime and Pi-UpTime.
2) Edit the file /etc/rc.local - we assume you have your favorite editor (nano, vi, emacs etc.) Make sure
   you use sudo to edit the file. For example, using nano, the command will be "sudo nano /etc/rc.local"
3) Add the following 2 lines just before the last line in /etc/rc.local - the last line in the file is exit 0

      \# Next line is for the operation of Pi-UpTime or PiZ-UpTime \
      sudo python /home/pi/uptime/uptime-2.0-rc-local.py &

     *exit 0      #  <-- Note this is the last line in the file /etc/rc.local*

4) Save the edited file /etc/rc.local and reboot

After reboot, the script is running in the background. No log messages are printed or stored.

To monitor the operating conditions at any *given instant* run the script in the file **uptime-2.0.py** using command "python uptime2.0.py"
Best to run this script with Python 2. Should also work with Python 3.
The polling frequency can be changed by changing the value of the variable ```tiempo``` in the script.

At any time you can hit Control C to terminate the program.
**_Please make sure you have commented / uncommented the line which measures the temperature, depending on whether you
 are using Pi-UpTime or PiZ-UpTime._**

 Contact support via https://alchemy-power.com/contact-us/ should you have any issues.

## Install Raspberry Pi OS (Raspbian) systemd Service

Configure uptime monitoring and auto shut-off using [systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md). This is an alternative to setting up /etc/rc.local, for Raspberry Pi OS Buster systems. Do not setup /etc/rc.local if you use the systemd method. Python 2 is at it's end of life, and is not supported: please use Python 3.

First you must enable the i2c ports using

    sudo raspi-config

Choose menu options:
* Interface Options / I2C / Yes *

To enable the systemd service when the Pi boots:

    # download this codebase
    git clone https://github.com/thrasher/uptime2.0.git

    # insure dependencies are installed (note: Buster Lite does not include these packages)
    sudo apt-get install python3-systemd python3-smbus

    # setup the service
    sudo ln -s `pwd`/uptime-2.0.service /etc/systemd/system/uptime-2.0.service
    sudo systemctl daemon-reload
    sudo systemctl enable uptime-2.0.service
    sudo systemctl start uptime-2.0.service

To stop the service:

    sudo systemctl stop uptime-2.0.service

Read and follow journal output from the process

    sudo journalctl -f -u uptime-2.0.service

Note that systemd services have some [documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html) you may want to read if modifying uptime-2.0.service.


