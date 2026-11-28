import json


def save_devices(devices, path="devices.json"):
    data = []
    for device in devices:
        # TODO: include type and class-specific fields
        data.append({"name": device.name})
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_devices(path="devices.json"):
    # TODO: reconstruct Sensor, Computer, and Printer objects
    with open(path, "r", encoding="utf-8") as file:
        return json.loda(file)
