# Headless Setup
Easily setup your Raspberry Pi by making changes to a mounted `boot` drive.


## Quick installation
```shell script
sudo python3 -m pip install git+git://github.com/retrodaredevil/headless-setup.git
```
Now run it!
```shell script
cd /media/$USER/boot # go to wherever the boot partition is mounted
headless-setup
```

## Features
* Can enable ssh by putting an `ssh` file in the boot drive
* Can set the WiFi credentials by creating a `wpa_supplicant.conf` file

---

### Local installation
Clone this and run (With sudo)
```shell script
python3 setup.py install
```

### Running without installing
```shell script
python3 headless_setup/__init__.py
```

### Links
* https://www.raspberrypi.org/documentation/remote-access/ssh/
* https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

### Finding IP Address
How to find your ip address: https://www.raspberrypi.org/documentation/remote-access/ip-address.md

However, usually the easiest thing is to run this command: `nmap -p 22 --open -sV 192.168.1.0/24` (assuming SSH is enabled)

### Future stuff to add
* Option to add `dtoverlay=disable-bt` to `config.txt` to disable bluetooth

