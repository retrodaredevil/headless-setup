# Headless Setup
Easily setup your Raspberry Pi by making changes to a mounted `boot` drive.

## Quick installation
Sudo is usually required for this on Linux
```shell script
python3 -m pip install git+git://github.com/retrodaredevil/headless-setup.git
```

## Local installation
Clone this and run (With sudo)
```shell script
python3 setup.py install
```
After installing you can run it (depending on permissions of your mounted boot partition, you may need sudo)
```shell script
headless-setup
```

## Running without installing
```shell script
python3 headless_setup/__init__.py
```

