class Device:
    """Parent class for all devices."""

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def needs_attention(self):
        return False

    def status(self):
        return "OK"

    def details(self):
        return f"{self.name} is located in {self.location}"

    def __str__(self):
        return f"{self.name} ({self.location}) - {self.status()}"


class Sensor(Device):
    def __init__(self, name, location, temperature):
        super().__init__(name, location)
        self.temperature = temperature

    def needs_attention(self):
        return self.temperature > 30

    def status(self):
        if self.needs_attention():
            return f"TOO HOT: {self.temperature}C"
        return f"Normal: {self.temperature}C"

    def details(self):
        return f"{self.name}: {self.temperature}C, limit 30C"


class Computer(Device):
    def __init__(self, name, location, online):
        super().__init__(name, location)
        self.online = online

    def needs_attention(self):
        return not self.online

    def status(self):
        return "Online" if self.online else "OFFLINE"


class Printer(Device):
    def __init__(self, name, location, toner):
        super().__init__(name, location)
        self.toner = toner

    def needs_attention(self):
        return self.toner < 15

    def status(self):
        if self.needs_attention():
            return f"LOW TONER: {self.toner}%"
        return f"Toner {self.toner}%"
