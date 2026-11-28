from devices import Device


class DeviceMonitor:
    def __init__(self, devices=None):
        self.devices = devices if devices is not None else []

    def add(self, device):
        if not isinstance(device, Device):
            raise TypeError("device must be a Device")
        self.devices.append(device)

    def remove(self, number):
        # TODO: finish validation and decide what remove should return
        del self.devices[number]

    def needing_attention(self):
        # TODO: complete filtering
        return [device for device in self.devices if device.needs_attentin()]

    def summary(self):
        # Deliberately incomplete.
        return None
