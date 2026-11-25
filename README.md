# Campus Device Monitor
A menu-driven Python program that tracks devices in a campus building
(sensors, computers, printers) and shows which ones need attention.

## Features
- Add, list, update and remove devices
- Highlights devices needing attention (hot sensor, offline/full computer, low-toner/no-paper printer)
- Data saved to `devices.json`
- Input validation on all prompts


## Files

 Main.py -- Menu and user input 
 devices.py --Device classes 
 monitor.py -- Manages the device collection 
 storage.py --  JSON save/load 
 tests/test_devices.py -- Unit tests 

## Run
python Main.py

## Test
python -m unittest discover tests

# UFP0007-M01152301
