# HorrorBoard

https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

Method 2: .bashrc

The second method to run a program on your Raspberry Pi at startup is to modify the .bashrc  file. With the .bashrc method, your python program will run when you log in (which happens automatically when you boot up and go directly to the desktop) and also every time when a new terminal is opened, or when a new SSH connection is made. Put your command at the bottom of ‘/home/pi/.bashrc’. The program can be aborted with ‘ctrl-c’ while it is running!

sudo nano /home/pi/.bashrc
Go to the last line of the script and add:

echo Running at boot 
sudo python /home/pi/Workspace/HorrorBoard/main.py &
The echo statement above is used to show that the commands in .bashrc file are executed on bootup as well as connecting to bash console.

Bash RC Configure systemd Run a Program On Your Raspberry Pi At Startup

Now reboot the Pi to hear the Pi speak at startup.

sudo reboot
The below image shows that the commands added to .bashrc file get executed even while opening a new terminal.

Bash RC Configure systemd Run a Program On Your Raspberry Pi At Startup