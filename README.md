# Pyshutdown

A simple gui wrapper to restart/shutdown the system. It's usefull for a windows manager like OpenBox that doesn't have that functionality.
It uses python & tkinter.

## Dependencies:

tk-inter
```sh
#apt-get install python-tk
```

## User grants
User need to be enough privilegies to shutdown/reboot the machine:

Create a new group:
```sh
sudo groupadd power
```
Adding your user to the group power:
```sh
sudo usermod -a -G power yourusername
```
Allow members of group power to shutdown without a password:
```sh
sudo visudo

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
# Allow members of group power to shutdown (or reboot) system
%power  ALL = NOPASSWD: /sbin/shutdown
```
It is necessary re-login to the changes take effect.

## Usage
pyshutdown.py [-h] [-l]
-h Show usage
-l Enable logging archive in /var/tmp/

## Language support
Pyshutdown detects the current user's language and the appropiate strings are showed. At this moment only english, spanish and german are supported.

| Language| User Interface |
| ------ | ------ |
|English (default)|![Screenshot English](https://user-images.githubusercontent.com/18613131/44646485-67d8e600-a9db-11e8-971a-a7f04531310d.png)|
|German|![Screenshot German](https://user-images.githubusercontent.com/18613131/44646484-67404f80-a9db-11e8-9def-c52bdbcc49c1.png)|
|Spanish|![Screenshot Spanish](https://user-images.githubusercontent.com/18613131/44646487-67d8e600-a9db-11e8-80a0-bfc11cc648e8.png)|

## Images credits
Images from [Mazenl77](http://www.iconarchive.com/artist/mazenl77.html)

| Original Image | Image on pyshutdown |
| ------ | ------ |
| [EZ Restart Icon](http://www.iconarchive.com/show/I-like-buttons-icons-by-mazenl77/EZ-Restart-icon.html)  | restart_48.png restart_64.png restart_128.png |
| [EZ Screen Saver Icon](http://www.iconarchive.com/show/I-like-buttons-icons-by-mazenl77/EZ-Screensaver-icon.html) | continue_48.png continue_64.png continue_128.png |
| [EZ Stand By Icon](http://www.iconarchive.com/show/I-like-buttons-icons-by-mazenl77/EZ-Standby-icon.html) | shutdown_48.png shutdown_64.png shutdown_64.png |
